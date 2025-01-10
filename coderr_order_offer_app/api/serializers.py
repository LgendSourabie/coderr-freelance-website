from rest_framework import serializers
from coderr_order_offer_app.models import Offer, OfferDetail, Order
from django.contrib.auth.models import User
from coderr_order_offer_app.api.utils import *


class UserDetailSerializer(serializers.ModelSerializer):
    """Serialize for further for nested usage in offer """

    first_name = serializers.SerializerMethodField()
    last_name =  serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['first_name','last_name','username']

    def get_first_name(self,profile:Profile):
        return profile.user.first_name

    def get_last_name(self,profile:Profile):
        return profile.user.last_name

    def get_username(self,profile:Profile):
        return profile.user.username
class OfferDetailSerializer(serializers.ModelSerializer):
        
    class   Meta:
        model = OfferDetail
        fields =  ['id','title','revisions', 'delivery_time_in_days', 'price','features','offer_type' ]

    def validate(self, attrs):
        features = attrs.get('features','')
        offer_type = attrs.get('offer_type','')
        delivery_time_in_days = attrs.get('delivery_time_in_days','')
        revisions = attrs.get('revisions','')

        # Validation for details
        if not isinstance(features, list):
            raise serializers.ValidationError({"detail":"Bitte eine Liste von Features angeben"})
        if not all(isinstance(item, str) for item in features):
            raise serializers.ValidationError({"detail":"Die einzelnen Features müssen String sein"})
        if not features:
            raise serializers.ValidationError({"detail":"Es muss mindestens ein Feature vorhanden sein"})
        
        # Validate Delivery time
        if delivery_time_in_days <=0:
            raise serializers.ValidationError({"detail":"Lieferzeit kann nicht negativ sein."})
        
        # Validate revision
        if revisions <-1:
            raise serializers.ValidationError({"detail":"Revision muss größer oder gleich -1 sein."})
        
        # Validation for offer_type
        
        if offer_type not in VALID_OFFER_TYPES:
            raise serializers.ValidationError({"detail":"Ungültiger Angebotstyp"})
        
        return attrs


class OfferSerializer(serializers.ModelSerializer):
  
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    user_details = UserDetailSerializer(source='user',read_only=True)
    image = serializers.ImageField(required=False, allow_null=True)
    details =  serializers.ListField(child=serializers.DictField(), write_only = True, required = True)
    min_price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, read_only=True)
    min_delivery_time = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Offer
        fields = ['id','user', 'title', 'image', 'description','created_at','updated_at','details', "min_price",'min_delivery_time','user_details']
        read_only_fields = ["min_price",'min_delivery_time','created_at','updated_at','user_details']

    def to_representation(self, instance):
        """Handle the read operation for detail since previously defined as write field."""

        request = self.context.get('request')

        data = super().to_representation(instance)
        detail_output = [
            {"id": detail_data.id, "url":f"/offerdetails/{detail_data.id}/"} for detail_data in instance.details.all()
        ]
        data['details'] = detail_output

        # Check if single offer query to customize output
        if request:
            print('REQUEST PATH', request.path)
            if str(instance.pk) in request.path:
                data['details'] = OfferDetailSerializer(instance.details.all(), many=True).data
        
        return data



    def validate(self, attrs):
        details = attrs.get('details','')
        image = attrs.get('image','')
        offer_details = [detail.get('offer_type') for detail in details]

        # Validate the image size and format
        max_file_size = 2 * 1024 * 1024

        # Verify if the file suze is not too large
        if image and image.size > max_file_size:
            raise serializers.ValidationError({"error":"Die Dateigröße übersteigt 2MB."})
        # Verify if the data format is allowed
        if image and not image.name.endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError({"error":"Ungültige Datei-Format"})
        
                
        if 'image' in attrs:
            image = attrs.pop('image', None)

        if self.instance and image:
            self.instance.image = image
            self.instance.save()

        #Validate offer details
        if len(details) != 3 and self.context.get('request').method == 'POST':
            raise serializers.ValidationError({"detail":"Angebot muss genau drei Pakete enthalten."})
        
        is_offer_type_and_create = set(offer_details) != SET_OFFER_TYPE and self.context.get('request').method == 'POST'
        is_offer_type_and_update = not set(offer_details).issubset(SET_OFFER_TYPE) and self.context.get('request').method == 'PATCH'
        
        if is_offer_type_and_create or is_offer_type_and_update:
            raise serializers.ValidationError({"detail":"Nur 'basic, standard oder premium' sind als Angebotstyp akzeptiert"})

        return attrs
    

    
    def create(self, validated_data):


        offer_details_data = validated_data.pop('details', [])

        validated_data['min_price'] = get_min_price(offer_details_data, method='post')
        validated_data['min_delivery_time'] = get_min_delivery_time(offer_details_data,method='post')

        # create offer
        offer = Offer.objects.create(**validated_data)
        
        offer_instances = []
        for details_data in  offer_details_data:

            if len(details_data["title"]) != 0:
                offer_detail_instance = OfferDetail.objects.create(**details_data)
                offer_instances.append(offer_detail_instance)
            else:
                raise serializers.ValidationError({"message":"Ungültige Eingabe"})
        offer.details.set(offer_instances)
        return offer

    def update(self, instance, validated_data):

        offer_details_data = validated_data.pop('details', [])
        offer_instances = list(instance.details.all())

        # Update of details
        if offer_details_data is not None and len(offer_details_data) <=3:
            for details_data in offer_details_data:
                offer_detail_id = details_data.get('id')
                if offer_detail_id:
                    try:
                        offer_detail_instance = next(detail for detail in offer_instances if detail.id == offer_detail_id )
                        serializer = OfferDetailSerializer(
                        offer_detail_instance, data=details_data, partial=True)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    except StopIteration:
                        raise serializers.ValidationError({"detail": f"Angebot mit Angebot-Detail ID {offer_detail_id} nicht gefunden."})
                else:
                    raise serializers.ValidationError({"detail":"Angebot muss genau drei Pakete enthalten. Geben Sie ein ID zur Aktualisierung von Angeboten."})

            instance.details.set(offer_instances)

        instance.refresh_from_db()

        #Update title, description, min price and delivery time
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.min_price = get_min_price(offer_instances)
        instance.min_delivery_time = get_min_delivery_time(offer_instances)

        instance.save()
        return instance  

class OrderSerializer(serializers.ModelSerializer):
    """Check data for consistency before saving them to the DB"""

    offer_detail = OfferDetailSerializer(read_only = True)
    offer_detail_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = Order
        fields = ['id','customer_user','business_user','offer_detail','offer_detail_id','status','created_at','updated_at']
        read_only_fields = ['customer_user','business_user','created_at','updated_at']

    def to_representation(self, instance):
        """Change the representation of data to meet frontend expectation"""

        old_data_representation = super().to_representation(instance)

        old_data_representation["title"] = instance.offer_detail.title
        old_data_representation["revisions"] = instance.offer_detail.revisions
        old_data_representation["delivery_time_in_days"] = instance.offer_detail.delivery_time_in_days
        old_data_representation["price"] = instance.offer_detail.price
        old_data_representation["features"] = instance.offer_detail.features
        old_data_representation["offer_type"] = instance.offer_detail.offer_type

        old_data_representation.pop('offer_detail')

        return old_data_representation
    

    def validate_offer_detail_id(self, id):
        "Check if there is any offer detail for provided ID"

        try:
            offer_details = OfferDetail.objects.get(pk = id)
        except:
            raise Exception("Not found")
        return id
    
    def get_business_user(self, order:Order):
        """Get the ID of owner of the offer/business user"""
        offer = order.offer_detail.offer.first()
        return offer.user.id if offer else None
    
class OrderCountSerializer(serializers.Serializer):

    class Meta:
        model = Order
        fields = '__all__'
