from django.urls import path
from . import views


urlpatterns = [
path('offers/',views.OfferList.as_view(), name='offers-list'),
path('offers/<int:pk>/',views.SingleOffer.as_view() ,name='offers-detail'),
path('offerdetails/<int:pk>/',views.SingleOfferDetail.as_view(),name='offerdetails-detail'),
path('orders/', views.OrderList.as_view(), name='orders-list'),
path('orders/<int:pk>/',views.SingleOrder.as_view(), name='orders-detail'),
path('order-count/<int:pk>/', views.OrderCount.as_view(),name='order-count'),
path('completed-order-count/<int:pk>/',views.CompletedOrderCount.as_view(), name='completed_order-count'),
]


