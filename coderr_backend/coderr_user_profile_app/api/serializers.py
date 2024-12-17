from rest_framework import serializers
from coderr_user_profile_app.models import Profile
from django.contrib.auth.models import User
from coderr_file_upload_app.api.serializers import FileUploadSerializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name']


class BusinessAndCustomerProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    file = FileUploadSerializer(read_only =True)
    class Meta:
        model = Profile
        fields = ['user', 'file', 'type']

    def to_representation(self, instance):
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]
        customer = Profile.PROFILE_TYPE_OPTIONS[1][1]
        current_representation = super().to_representation(instance)

        try:
            uploaded_data_value_json = list(instance.fileupload_set.values()).pop()
        except IndexError:
            current_representation['file'] = 'null'
            upload_date = 'null'
        else:
            current_representation['file'] = uploaded_data_value_json['file']
            upload_date = uploaded_data_value_json['uploaded_at']


        if instance.type == business:
            current_representation['location'] = instance.location
            current_representation['tel'] = instance.tel
            current_representation['description'] = instance.description
            current_representation['working_hours'] = instance.working_hours
        if instance.type == customer:
            current_representation['uploaded_at'] =upload_date

        return current_representation

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user','location','tel','description','working_hours', 'type', 'created_at']

    def to_representation(self, instance):
        current_representation = super().to_representation(instance)
        current_representation['username'] = instance.user.username
        current_representation['first_name'] = instance.user.first_name
        current_representation['last_name'] = instance.user.last_name
        current_representation['email'] = instance.user.email
        current_representation['username'] = instance.user.username

        return current_representation



