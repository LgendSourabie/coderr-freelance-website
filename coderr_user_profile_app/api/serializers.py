from rest_framework import serializers
from coderr_user_profile_app.models import Profile
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username','first_name','last_name']


class BusinessAndCustomerProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    file = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = Profile
        fields = ['user', 'file', 'type']

    def to_representation(self, instance):
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]
        customer = Profile.PROFILE_TYPE_OPTIONS[1][1]
        current_representation = super().to_representation(instance)

        if instance.file:
            current_representation['file'] = instance.file.url
        if instance.type == business:
            current_representation['location'] = instance.location
            current_representation['tel'] = instance.tel
            current_representation['description'] = instance.description
            current_representation['working_hours'] = instance.working_hours
        if instance.type == customer:
            current_representation['uploaded_at'] =instance.uploaded_at
        return current_representation

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only = True)
    file = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = ['user','file','location','tel','description','working_hours', 'type', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    

    def to_representation(self, instance):

        current_representation = super().to_representation(instance)
        
        current_representation['username'] = instance.user.username
        current_representation['first_name'] = instance.user.first_name
        current_representation['last_name'] = instance.user.last_name
        current_representation['email'] = instance.user.email
        return current_representation
    
    def validate(self, attrs):
        file = attrs.get('file','')

        # Validate the image size and format
        max_file_size = 2 * 1024 * 1024
       
        # Verify if the file suze is not too large
        if file and file.size > max_file_size:
            raise serializers.ValidationError({"error":"Die Dateigröße übersteigt 2MB."})
        
        # Verify if the data format is allowed
        if file and not file.name.endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError({"error":"Ungültige Datei-Format"})
        return attrs
        
  
    def update(self, instance, validated_data):

        user_instance = instance.user
        updated_data = self.context.get('request').data
        username = updated_data.get('username')
        first_name = updated_data.get('first_name')
        last_name = updated_data.get('last_name')
        email = updated_data.get('email')

        # Update the user data
        if user_instance:
            if username:
                user_instance.username = username
            if first_name:
                user_instance.first_name = first_name
            if last_name:
                user_instance.last_name = last_name
            if email:
                user_instance.email = email

            user_instance.save()

        # update the other profile data
        instance.location = validated_data.get('location', instance.location)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.description = validated_data.get('description', instance.description)
        instance.working_hours = validated_data.get('working_hours', instance.working_hours)
        
        if 'file' in validated_data:
            instance.file = validated_data['file']
        instance.save()
        return instance
    
    




