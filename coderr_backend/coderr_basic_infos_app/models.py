from django.db import models
from django.contrib.auth.models import User
from coderr_user_profile_app.models import Profile
# Create your models here.

class Rating(models.Model):

    business_user =  models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='business_ratings')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviewer_ratings')
    rating = models.SmallIntegerField()
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.reviewer.user.username} {self.rating}"
    