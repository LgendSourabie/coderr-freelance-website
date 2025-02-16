from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import login
from rest_framework.response import Response
from coderr_auth_app.api.serializers import LoginSerializer, RegistrationSerializer
from coderr_auth_app.api.utils import *


class Login(ObtainAuthToken):
    """Users can log in using their username and password
    
    Keyword arguments:
    argument -- username - username given during the registration
    Return: {username, email, token, user_id}
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        request_data = request.data
        
        if request_data and is_customer_guest(request_data):
           log_data = guest_login(request=request, profile_type="customer")
           return Response(log_data, status=status.HTTP_200_OK)
        elif request_data and is_business_guest(request_data):
            log_data = guest_login(request=request, profile_type="business")
            return Response(log_data, status=status.HTTP_200_OK)

        else:
        # if request
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                validated_user = serializer.validated_data['user']
                token, _ = Token.objects.get_or_create(user=validated_user)

                login(request,validated_user)

                user_data = {
                    "token":token.key,
                    "username":validated_user.username,
                    "email":validated_user.email,
                    "user_id":validated_user.id
                }
                return Response(user_data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Registration(APIView):
    """Registration of new user"""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data =request.data )
        
        if serializer.is_valid():
            saved_account = serializer.save()
            token, _ = Token.objects.get_or_create(user=saved_account)
            data={
                "token":token.key,
                "username":saved_account.username,
                "email":saved_account.email,
                "user_id":saved_account.id
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)