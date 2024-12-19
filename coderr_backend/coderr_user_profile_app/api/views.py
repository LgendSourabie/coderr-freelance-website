from rest_framework import generics
from coderr_user_profile_app.models import Profile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from coderr_order_offer_app.api.utils import get_model_or_exception
from coderr_user_profile_app.api.serializers import ProfileSerializer, BusinessAndCustomerProfileSerializer
from coderr_user_profile_app.api.permissions import IsOwnerOrAdmin


class CustomerProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = BusinessAndCustomerProfileSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        customer = Profile.PROFILE_TYPE_OPTIONS[1][1]
        customer_profiles = Profile.objects.filter(type=customer)

        serializer = self.get_serializer(customer_profiles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)   
    

    

class BusinessProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = BusinessAndCustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]
        business_profiles = Profile.objects.filter(type=business)

        serializer = self.get_serializer(business_profiles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    

class ProfileDetail(generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrAdmin]


    def get(self, request, pk):
        profile = get_model_or_exception(Profile,pk, 'Kein Profil gefunden.')

        # profile = user.profile

        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_serializer_context(self):
        return {'request': self.request}
    

    def patch(self, request, pk):
        profile = get_model_or_exception(Profile,pk, "Kein Profil gefunden.")
        
        serializer = ProfileSerializer(profile, data = request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    