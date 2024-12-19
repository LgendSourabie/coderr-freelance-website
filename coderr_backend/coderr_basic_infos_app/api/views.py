from coderr_order_offer_app.models import Offer
from coderr_user_profile_app.models import Profile
from rest_framework import generics, status
from rest_framework.response import Response
from coderr_basic_infos_app.models import Rating
from coderr_basic_infos_app.api.serializers import RatingSerializer
from coderr_basic_infos_app.api.utils import calculate_average_rating
from coderr_basic_infos_app.api.filters import RatingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from coderr_basic_infos_app.api.permissions import IsCustomerAndAuthenticated



class BaseInfoList(generics.ListAPIView):
    queryset = Offer.objects.all()

    def get(self, request, *args, **kwargs):

        business = Profile.PROFILE_TYPE_OPTIONS[0][0]
        ratings = Rating.objects.all().values_list('rating', flat=True)
        rating_list = list(ratings)

        data = {
                "review_count": len(Rating.objects.all()),
                "average_rating": calculate_average_rating(rating_list),
                "business_profile_count": len(Profile.objects.filter(type=business)),
                "offer_count": len(Offer.objects.all()),
              }
        return Response(data, status=status.HTTP_200_OK)
    


class ReviewsList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsCustomerAndAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RatingFilter
    ordering_fields = ['updated_at','rating']


    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(reviewer = self.request.user.profile)


class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    permission_classes = IsCustomerAndAuthenticated
    serializer_class = RatingSerializer
    

