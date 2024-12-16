from coderr_order_offer_app.models import Offer
from coderr_user_profile_app.models import Profile
from rest_framework import generics, status
from rest_framework.response import Response
from coderr_basic_infos_app.models import Rating
from coderr_basic_infos_app.api.serializers import RatingSerializer




class BaseInfoList(generics.ListAPIView):
    queryset = Offer.objects.all()

    def get(self, request, *args, **kwargs):


        number_offer = len(Offer.objects.all())

        data = {
                "review_count": 10,
                "average_rating": 4.6,
                "business_profile_count": 45,
                "offer_count": number_offer,
              }
        return Response(data, status=status.HTTP_200_OK)
    


class ReviewsList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    

