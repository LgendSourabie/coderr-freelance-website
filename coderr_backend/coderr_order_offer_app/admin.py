from django.contrib import admin
from coderr_order_offer_app.models import Offer, OfferDetail, Order

admin.site.register(Offer)
admin.site.register(Order)
admin.site.register(OfferDetail)