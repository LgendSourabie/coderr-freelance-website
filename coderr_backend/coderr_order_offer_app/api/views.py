from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from coderr_order_offer_app.api.throttles import HundredCallsPerSecond
from coderr_order_offer_app.api.utils import is_order_for_business_user, is_order_in_progress,\
                                             get_model_or_exception
from coderr_order_offer_app.models import OfferDetail, Offer, Order
from coderr_user_profile_app.models import Profile
from django.contrib.auth.models import User
from coderr_order_offer_app.api.permissions import IsBusinessAndAuthenticated, IsAuthorized,\
                                                   IsBusinessUser, IsBusinessAndOwner
from django_filters.rest_framework import DjangoFilterBackend
from coderr_order_offer_app.api.filters import OfferFilter
from coderr_order_offer_app.api.paginations import OfferPagination
from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.db.models import Q
from .serializers import OfferDetailSerializer, OfferSerializer, OrderSerializer, OrderCountSerializer

class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsBusinessAndAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class = OfferFilter
    pagination_class = OfferPagination
    throttle_classes = [HundredCallsPerSecond]
    ordering_fields=['min_price','updated_at']
    search_fields = ['title','description']


    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user = self.request.user.profile)

    def create(self, request, *args, **kwargs):
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]

        if self.request.user.profile.type != business:
            return Response({"error":"Nur Geschäftsnutzer können Angebote erstellen."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
class SingleOffer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsBusinessAndOwner]
    throttle_classes = [HundredCallsPerSecond]

    def get(self, request, pk):
        offer = get_model_or_exception(Offer,pk, 'Kein Angebot gefunden.')
        serializer = OfferSerializer(offer, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_serializer_context(self):
        return {'request': self.request}

    def patch(self, request, pk):
        offer = get_model_or_exception(Offer,pk, "Kein Angebot gefunden.")
        serializer = OfferSerializer(offer, data = request.data, partial=True, context={'request': request})

        if offer.user == request.user.profile or request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail":"Du hast keine Berechtigung für diese Operation."},status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request,pk):
        offer = get_model_or_exception(Offer,pk, "Kein Angebot gefunden.")

        if offer.user != request.user.profile or not request.user.is_superuser:
            return Response({"detail":"Du hast keine Berechtigung für diese Operation."}, status=status.HTTP_401_UNAUTHORIZED)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SingleOfferDetail(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer   
    permission_classes = [IsBusinessAndOwner]
    throttle_classes = [HundredCallsPerSecond]


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthorized]
    throttle_classes = [HundredCallsPerSecond]
    

    def perform_create(self, serializer):
        if serializer.is_valid():
            offer_detail_id = serializer.validated_data.get('offer_detail_id')
            offer_detail = get_model_or_exception(OfferDetail, offer_detail_id, "Angebot nicht gefunden.")
            business_user = offer_detail.offer.first().user
            serializer.save(customer_user = self.request.user.profile, business_user = business_user)


    def list(self, request, *args, **kwargs):

        if request.user.is_superuser:
            data = Order.objects.all()
        else:
            data = Order.objects.filter(Q(business_user=request.user.profile) | Q(customer_user=request.user.profile))
        serializer = OrderSerializer(data, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBusinessUser]
    throttle_classes = [HundredCallsPerSecond]


class OrderCount(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCountSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):

        business_user_orders_in_progress = []
        business_user = get_model_or_exception(Profile, pk,'Geschäftsnutzer nicht gefunden.')

        for order in Order.objects.all():
            if is_order_for_business_user(order, business_user) and is_order_in_progress(order):
                business_user_orders_in_progress.append(order)
        return Response({"order_count":len(business_user_orders_in_progress)} , status=status.HTTP_200_OK) 



class CompletedOrderCount(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCountSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):

        business_user_orders_completed = []
        business_user = get_model_or_exception(User, pk,'Geschäftsnutzer nicht gefunden')

        for order in Order.objects.all():
            if is_order_for_business_user(order, business_user) and not is_order_in_progress(order):
                business_user_orders_completed.append(order)
        return Response({"completed_order_count":len(business_user_orders_completed)} , status=status.HTTP_200_OK) 
    