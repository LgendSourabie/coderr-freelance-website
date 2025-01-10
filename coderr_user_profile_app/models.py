from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ 
    Profile is a which corresponds to a customer or business profile type.
    The Profile will be generated when the user registers or signs up. 
    """
    PROFILE_TYPE_OPTIONS = (('business','business'),('customer','customer'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    file = models.ImageField(upload_to='uploads/profiles/',blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True, default="")
    tel = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(max_length=300, blank=True, default="")
    working_hours = models.CharField(max_length=10, blank=True, default="")
    type = models.CharField(max_length=50, choices=PROFILE_TYPE_OPTIONS, default='customer')

    def __str__(self):
        return f"{self.user.username}'s {self.type} profile"
    