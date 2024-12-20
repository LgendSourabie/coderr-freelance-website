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
from coderr_order_offer_app.api.utils import get_model_or_exception
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
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
            business_user_profile = serializer.validated_data.get('business_user')
            business_user = get_model_or_exception(Profile, business_user_profile.id, "Geschäftsnutzer nicht gefunden.")
            serializer.save(reviewer = self.request.user.profile, business_user = business_user)


class ReviewsDetail(APIView):

    def check_object_permission(self, request, rating):
        if not IsCustomerAndAuthenticated().has_object_permission(request, self, rating):
            raise PermissionDenied("Du hast keine Berechtigung, um diese Operation zu tun.")
    
    def get(self, request, pk):
        rating = get_model_or_exception(Rating, pk, 'Bewertung nicht gefunden')
        self.check_object_permission(request, rating)
        serializer = RatingSerializer(rating,context={'request': request})
        return Response(serializer.data)
    
    def patch(self, request, pk):
        rating = get_model_or_exception(Rating, pk, 'Bewertung nicht gefunden')
        self.check_object_permission(request, rating)

        serializer = RatingSerializer(rating, data=request.data, partial=True,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        rating = get_model_or_exception(Rating, pk, 'Bewertung nicht gefunden')
        self.check_object_permission(request, rating)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rating.objects.all()
#     permission_classes = [IsCustomerAndAuthenticated]
#     serializer_class = RatingSerializer

    