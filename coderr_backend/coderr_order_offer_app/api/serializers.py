from rest_framework import serializers
from coderr_order_offer_app.models import Offer, OfferDetail, Order
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from coderr_order_offer_app.api.utils import *


class UserDetailSerializer(serializers.ModelSerializer):
    """Serialize for further for nested usage in offer """
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
class OfferDetailSerializer(serializers.ModelSerializer):
        
    class   Meta:
        model = OfferDetail
        fields =  ['id','title','revisions', 'delivery_time_in_days', 'price','features','offer_type' ]
        extra_kwargs = {
            "revisions":{"min_value":-1},
            "delivery_time_in_days":{"min_value":1},
        }

    def validate(self, attrs):
        features = attrs.get('features','')
        offer_type = attrs.get('offer_type','')

        # Validation for details
        if not isinstance(features, list):
            return serializers.ValidationError("Bitte eine Liste von Features angeben")
        if not all(isinstance(item, str) for item in features):
            return serializers.ValidationError("Die einzelnen Features müssen String sein")
        if not features:
            return serializers.ValidationError("Es muss mindestens ein Feature vorhanden sein")
        
        # Validation for offer_type
        
        if offer_type not in VALID_OFFER_TYPES:
            return serializers.ValidationError("Ungültiger Typ von Angebot")
        
        return attrs


class OfferSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    user_details = UserDetailSerializer(source='user',read_only=True)
    details =  serializers.ListField(child=serializers.DictField(), write_only = True, required = True)
    min_price = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, read_only=True)

    class Meta:
        model = Offer
        fields = ['id','user', 'title', 'image', 'description','created_at','updated_at','details', "min_price",'user_details']
        read_only_fields = ['created_at','updated_at']
        depth = 1

    def to_representation(self, instance):
        """Handle the read operation for detail since previously defined as write field."""

        data = super().to_representation(instance)
        detail_output = [
            {"id": detail_data.id, "url":f"/offerdetails/{detail_data.id}/"} for detail_data in instance.details.all()
        ]
        data['details'] = detail_output
        # data['details'] = OfferDetailSerializer(instance.details.all(), many=True).data
        return data
    

    def get_min_price(self, details):
        all_detail_price = [price['price'] for price in details]

        return min(all_detail_price)


    def get_min_delivery_time(self):
        pass


    def validate(self, attrs):
        details = attrs.get('details','')
        offer_details = [detail.get('offer_type') for detail in details]
    

        #Validate offer details
        if len(details) != 3:
            return serializers.ValidationError("Angebot muss genau drei Pakete enthalten")
        
        if set(offer_details) != SET_OFFER_TYPE:
            return serializers.ValidationError("Ungültige eingabe")
        
        return attrs
    
    def create(self, validated_data):

        offer_details_data = validated_data.pop('details', [])
        min_price = self.get_min_price(offer_details_data)
        validated_data['min_price'] = min_price

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
        offer_details_data = validated_data.pop('details', None)

        instance = super().update(instance, validated_data)

        offer_instances = []
        request = self.context.get('request')


        if offer_details_data is not None:
            for details_data in offer_details_data:
                offer_detail__id = details_data.get('id')
                if offer_detail__id:
                    offer_detail_instance = OfferDetail.objects.get(id=offer_detail__id)
                    offer_detail_instance.title = details_data.get('title', offer_detail_instance.title)
                    offer_detail_instance.revisions = details_data.get('revisions', offer_detail_instance.revisions)
                    offer_detail_instance.delivery_time_in_days = details_data.get('delivery_time_in_days', offer_detail_instance.delivery_time_in_days)
                    offer_detail_instance.price = details_data.get('price', offer_detail_instance.price)
                    offer_detail_instance.features = details_data.get('features', offer_detail_instance.features)
                    offer_detail_instance.offer_type = details_data.get('offer_type', offer_detail_instance.offer_type)
                    offer_detail_instance.save()
                else:
                    offer_detail_instance = OfferDetail.objects.create(**details_data)
                offer_instances.append(offer_detail_instance)

            instance.details.set(offer_instances)

        instance.refresh_from_db()

        return instance  

class OrderSerializer(serializers.ModelSerializer):
    """Check data for consistency before saving them to the DB"""
    
    customer_user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
             )

    offer_detail = OfferDetailSerializer(read_only = True)
    offer_detail_id = serializers.IntegerField(write_only = True)
    business_user = serializers.SerializerMethodField(method_name='get_business_user')

    class Meta:
        model = Order
        fields = ['id','customer_user','business_user','offer_detail','offer_detail_id','status','created_at','updated_at']


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
