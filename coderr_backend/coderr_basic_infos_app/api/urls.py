from django.urls import path
from . import views


urlpatterns = [
    path('base-info/',views.BaseInfoList.as_view(), name='base-info'),
    path('reviews/',views.ReviewsList.as_view(),name='reviews-list'),
    path('reviews/<int:pk>/',views.ReviewsDetail.as_view(),name='reviews-list'),
]
