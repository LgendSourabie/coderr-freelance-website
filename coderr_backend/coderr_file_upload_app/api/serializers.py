from rest_framework import serializers
from coderr_file_upload_app.models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['file', 'uploaded_at']

    def create(self, validated_data):
        validated_data['profile'] = self.context['request'].user.profile
        return super().create(validated_data)
