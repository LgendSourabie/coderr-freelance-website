from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """ 
    Profile is a standard profile which correspond to a customer profile.
        - file: profile picture of a customer or a businessman if inherited by BusinessProfile class.
        - uploaded_at : date the picture has been uploaded
        - type: type of profile - is either customer or business
    """
    PROFILE_TYPE_OPTIONS = (('business','business'),('customer','customer'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # file = models.FileField(upload_to='/', blank=True, null=True)
    # uploaded_at = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null= True)
    tel = models.CharField(max_length=50, blank=True, null= True)
    description = models.TextField(max_length=300, blank=True, null= True)
    working_hours = models.CharField(max_length=10, blank=True, null= True)
    type = models.CharField(max_length=50, choices=PROFILE_TYPE_OPTIONS, default='customer')

    def __str__(self):
        return f"{self.user.username} has a {self.type} profile"

