from django.http import Http404
from coderr_order_offer_app.models import OfferDetail, Offer, Order
from .serializers import OfferDetailSerializer, OfferSerializer, OrderSerializer, OrderCountSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from coderr_order_offer_app.api.utils import is_order_for_business_user, is_order_in_progress,\
                                                get_model_or_exception
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields=['min_price','updated_at']
    search_fields = ['title']
    filterset_fields=['min_price']


class SingleOffer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class SingleOfferDetail(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer   


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SingleOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]



class OrderCount(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCountSerializer

    def get(self, request, pk):

        business_user_orders_in_progress = []

        business_user = get_model_or_exception(User, pk,'Business user')

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

        business_user = get_model_or_exception(User, pk,'Business user')

        for order in Order.objects.all():
            if is_order_for_business_user(order, business_user) and not is_order_in_progress(order):
                business_user_orders_completed.append(order)

        return Response({"completed_order_count":len(business_user_orders_completed)} , status=status.HTTP_200_OK) 
    