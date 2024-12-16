from django.db import models
from django.contrib.auth.models import User
from coderr_order_offer_app.api.utils import *
# Create your models here.



class OfferDetail(models.Model):
    """
    Detail of Offer of business users. 
    
        title: title of the offer detail
        revisions: number of revisions included in the offer
        delivery_time_in_days: maximal time for delivery (in days)
        price: price of the offer
        features: list of features included in the offer
        offer_type: type of the offer
    """

    title = models.CharField(max_length=50)
    revisions = models.SmallIntegerField(default=-1)
    delivery_time_in_days = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    features = models.JSONField()
    offer_type = models.CharField(max_length=8,choices=OFFER_TYPE_OPTIONS,default='basic', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.price}"


class Offer(models.Model):
    """
    Offer of business users. An offer consists of three details ('basic','standard','premium')
    
        title: title of the offer
        image: picture of the offer for overview
        description: description of the offer
        created_at: date on which the offer was released for the first time
        updated_at: date of the last update of the offer
        user: user which created or is owner of the offer
        details: array of exactly three detail as mentioned previously
    """
    
    title = models.CharField(max_length=50)
    # image = models.ForeignKey(FileUpload, on_delete=models.PROTECT)
    image = models.FileField(upload_to='uploads',blank=True, null=True)
    description = models.TextField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.ManyToManyField(OfferDetail, related_name='offer')
    min_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.min_price}"
    
    def delete(self, *args, **kwargs):
        self.details.all().delete()
        return super().delete(*args, **kwargs)

    
class Order(models.Model):
    """
    Order of customers
    """
    
    offer_detail = models.ForeignKey(OfferDetail, on_delete=models.CASCADE)
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15,choices=ORDER_STATUS_OPTIONS, default="in_progress") 
