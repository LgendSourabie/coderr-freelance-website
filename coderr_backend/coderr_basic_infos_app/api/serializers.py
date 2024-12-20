from rest_framework import serializers
from coderr_user_profile_app.models import Profile
from coderr_basic_infos_app.models import Rating
from coderr_order_offer_app.api.utils import get_model_or_exception
from django.db import IntegrityError


class RatingSerializer(serializers.ModelSerializer):
     
    rating = serializers.IntegerField(allow_null =True)
    description =serializers.CharField(max_length=300, allow_blank = True)
    class Meta:
        model = Rating
        fields = ['id','business_user','reviewer','rating','description','created_at','updated_at']
        read_only_fields = ['reviewer','created_at','updated_at']


    def create(self, validated_data):
        business_user_id = validated_data['business_user']

        # Check Business user if it there is any user with provided ID
        business_user = get_model_or_exception(Profile, business_user_id.id,'Geschäftsnutzer nicht gefunden.')

        # Validate if the reviewer is actually a customer user
        customer = Profile.PROFILE_TYPE_OPTIONS[1][1]
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]

        if self.context['request'].user.profile.type != customer:
            raise serializers.ValidationError({"error": "Nur Kundennutzer dürfen eine Bewertung durchführen."})
        if business_user.type != business:
            raise serializers.ValidationError({"error": "Nur Geschäftsnutzer können bewertet werden."})

        # Check if the reviewer user has already rated the business user
        try:
            super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"error":"Sie haben schon diesen Geschäftsnutzer bewertet."})
        return validated_data
    

    def update(self, instance, validated_data):
        business_user = validated_data.get('business_user',None)
        if business_user:
            raise serializers.ValidationError({"error":"Ungültige oder fehlende Felder."})
        return super().update(instance, validated_data)
        
    def validate(self, attrs):
        rating = attrs.get('rating')
        description = attrs.get('description')

        # Validation Description if given and not whitespace
        if not description or len(description) == 0:
            raise serializers.ValidationError({"error":"Das Feld 'description' ist pflicht."})
        
        # Validate if provided value is an integer
        if not isinstance(rating, int):
             raise serializers.ValidationError({"error":"Ungültige Bewertungseingabe."})

        # Validation of rating if between 0-5
        if rating <0 or rating > 5:
            raise serializers.ValidationError({"error":"Bewertung muss zwischen 0 und 5 liegen."})
        return attrs
