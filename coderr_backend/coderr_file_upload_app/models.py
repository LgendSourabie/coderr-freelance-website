from django.db import models
from coderr_user_profile_app.models import Profile
# Create your models here.

class FileUpload(models.Model):
    file = models.FileField(upload_to='',blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)