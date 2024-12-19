

from django_filters.rest_framework import filters
from django_filters import FilterSet
from coderr_order_offer_app.models import Offer

class OfferFilter(FilterSet):
    creator_id = filters.NumberFilter(field_name="user", lookup_expr="exact")
    min_price = filters.NumberFilter(field_name="min_price", lookup_expr="gte")

    class Meta:
        model = Offer
        fields = ["creator_id","min_price"]