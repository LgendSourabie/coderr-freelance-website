from rest_framework import generics
from coderr_user_profile_app.models import Profile,BusinessProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from coderr_user_profile_app.api.serializers import ProfileSerializer, BusinessProfileSerializer
from coderr_user_profile_app.api.permissions import IsOwnerOrAdmin



class CustomerProfileList(generics.ListAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        customer = Profile.PROFILE_TYPE_OPTIONS[1][1]
        customer_profiles = Profile.objects.filter(type=customer)
        return Response(customer_profiles, status=status.HTTP_200_OK)
    

class BusinessProfileList(generics.ListAPIView):

    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        business = Profile.PROFILE_TYPE_OPTIONS[0][0]
        business_profiles = Profile.objects.filter(type=business)
        return Response(business_profiles, status=status.HTTP_200_OK)
    
    

class ProfileDetail(generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrAdmin]


    def get_profile_or_404(self, pk):
        try:
            profile = Profile.objects.get(pk = pk)
            return profile
        except Profile.DoesNotExist:
            return Response({'error_message':'Profil nicht gefunden'}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk):
        profile = self.get_profile_or_404(pk)

        serializer = ProfileSerializer(data=profile)
     
        data ={
                "user": profile.user.id,
                "username": profile.user.username,
                "first_name": profile.user.first_name,
                "last_name":profile.user.last_name,
                "file":profile.file.name if profile.file.name else 'null',
                "type": profile.type,
                "email": profile.user.email,
                "created_at": profile.created_at
                }   
        
        if profile.type == 'business':
            data.update( {
                    "location": profile.location,
                    "tel":profile.tel,
                    "description": profile.description,
                    "working_hours": profile.working_hours
                    })

        return Response(data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):
        profile = self.get_profile_or_404(pk)
        
        serializer = ProfileSerializer(data = request.data)
        if profile.type == 'business':
            serializer = BusinessProfileSerializer

        if serializer.is_valid():
            serializer.save()

        

