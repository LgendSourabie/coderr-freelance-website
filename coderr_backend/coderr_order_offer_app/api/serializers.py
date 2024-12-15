from rest_framework import serializers
from coderr_order_offer_app.models import Offer, OfferDetail, Order
from django.contrib.auth.models import User
from coderr_order_offer_app.api.utils import *



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
    details = OfferDetailSerializer(many=True)
    # details = OfferDetailSerializer(many=True, read_only = True)
    # offer_details =  serializers.ListField(child=serializers.DictField(), write_only = True, required = True)

    class Meta:
        model = Offer
        fields = ['id','user', 'title', 'image', 'description','created_at','updated_at','details']
        read_only_fields = ['created_at','updated_at']
        depth = 1

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

        detail_data = validated_data.pop('details')
        offer = Offer.objects.create(**validated_data)
        
        for detail in detail_data:
            OfferDetail.objects.create(offer=offer, **detail_data)
    

class OrderSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Offer
        fields = ['id']

