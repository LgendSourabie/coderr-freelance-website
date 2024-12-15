from django.urls import path
from . import views


urlpatterns = [
path('offers/', name='offers-list'),
path('offers/<int:id>/', name='offers-detail'),
path('offerdetails/<int:id>/', name='offerdetails-detail'),
path('orders/', name='orders-list'),
path('orders/<int:id>/', name='orders-detail'),
path('order-count/<int:business_user_id>/', name='order-count'),
path('completed_order-count/<int:business_user_id>/', name='completed_order-count'),
]


