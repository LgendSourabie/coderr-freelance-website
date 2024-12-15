from rest_framework import serializers
from coderr_user_profile_app.models import Profile, BusinessProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username','first_name','last_name']



class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'file' ,'uploaded_at', 'type']


class BusinessProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = BusinessProfile
        fields = ['user', 'file','location','tel','description','working_hours', 'type']