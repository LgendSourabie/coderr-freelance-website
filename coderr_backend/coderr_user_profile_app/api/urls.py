from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/',views.ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/business/',views.CustomerProfileList.as_view(), name='business-profiles-list'),
    path('profiles/customer/',views.BusinessProfileList.as_view(), name='customer-profiles-list'),
]
