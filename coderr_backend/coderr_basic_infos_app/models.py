from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rating(models.Model):

    business_user =  models.IntegerField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)