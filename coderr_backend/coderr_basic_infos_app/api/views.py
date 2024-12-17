from coderr_order_offer_app.models import Offer
from coderr_user_profile_app.models import Profile
from rest_framework import generics, status
from rest_framework.response import Response
from coderr_basic_infos_app.models import Rating
from coderr_basic_infos_app.api.serializers import RatingSerializer
from coderr_basic_infos_app.api.utils import calculate_average_rating



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

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(reviewer = self.request.user)

class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    

