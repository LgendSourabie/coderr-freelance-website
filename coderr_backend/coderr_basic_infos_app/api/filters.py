
from django_filters.rest_framework import filters
from django_filters import FilterSet
from coderr_basic_infos_app.models import Rating

class RatingFilter(FilterSet):
    business_user_id = filters.NumberFilter(field_name="business_user", lookup_expr="exact")
    reviewer_id = filters.NumberFilter(field_name="reviewer", lookup_expr="exact")

    class Meta:
        model = Rating
        fields = ["business_user_id","reviewer_id"]