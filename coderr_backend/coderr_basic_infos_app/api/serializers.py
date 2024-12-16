from rest_framework import serializers
from coderr_basic_infos_app.models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from coderr_order_offer_app.api.utils import get_model_or_exception



class RatingSerializer(serializers.ModelSerializer):
     

    business_user = serializers.IntegerField()
    reviewer = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default= serializers.CurrentUserDefault()
    )

    rating = serializers.IntegerField()
    description =serializers.CharField(max_length=300, allow_blank = True)

    class Meta:
        model = Rating
        fields = ['id','business_user','reviewer','rating','description','created_at','updated_at']
        validators =  [
                UniqueTogetherValidator(
                    queryset=Rating.objects.all(),
                    fields= ['business_user','reviewer']
                )
            ]
        
    def validate(self, attrs):
        rating = attrs.get('rating')
        description = attrs.get('description')
        business_user_id = attrs.get('business_user')

        # Validation Business user if it there is any user with provided ID
        business_user = get_model_or_exception(User, business_user_id)

        # Validate if the user is actually a business user
        # if business_user


        # Validate if the reviewer is actually a customer user

        # Validate value of ID/Business_user if it is positive and greater than 0
        if business_user_id <= 0:
            raise serializers.ValidationError({"error":"Ungültige ID, ID muss größer als 0 sein."})


        # Validation Description if given and not whitespace
        if not description or len(description) == 0:
            raise serializers.ValidationError({"error":"Das Feld 'description' ist pflicht."})

        # Validation of rating if between 0-5
        if rating <0 or rating > 5:
            raise serializers.ValidationError({"error":"Bewertung muss zwischen 0 und 5 liegen."})
        return attrs
