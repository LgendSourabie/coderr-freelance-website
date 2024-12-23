from django.db import models
from coderr_user_profile_app.models import Profile

class Rating(models.Model):

    business_user =  models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='business_ratings')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviewer_ratings')
    rating = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reviewer.user.username} rates {self.business_user.user.username} with {self.rating}"
    
    class Meta:
        unique_together = ('reviewer','business_user')
    