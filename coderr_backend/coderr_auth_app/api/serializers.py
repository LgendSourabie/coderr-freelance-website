from rest_framework import serializers
from django.contrib.auth.models import User
from coderr_user_profile_app.models import Profile
from django.contrib.auth import authenticate




class LoginSerializer(serializers.Serializer):
    """ 
    Login serializer for secure form data sent. 
    Login can be done through username and password
    """

    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username", None)
        password = attrs.get("password", None)


        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Falsche Anmeldeinformationen oder ungültige Eingabe.")

        user = authenticate(username=username, password=password)

        if user is None or not user.is_active:
            raise serializers.ValidationError("Falsche Anmeldeinformationen oder ungültige Eingabe.")
        
        attrs['user'] = user

        return attrs
    

class RegistrationSerializer(serializers.ModelSerializer):
    """"
    User registration serializer allowing to save clean data into DB. 

    """
    repeated_password = serializers.CharField(write_only = True)
    type = serializers.ChoiceField(choices=Profile.PROFILE_TYPE_OPTIONS)
   
    class Meta:
        model = User
        fields = ['username','email','password','repeated_password', 'type']
        extra_kwargs = {
            "password":{
                "write_only":True
            }
         
        }


    def validate(self, data):
        
        has_pwd_match = data["password"] == data["repeated_password"]
        entered_email = data['email']
        entered_username = data["username"]
        email_exist = User.objects.filter(email=entered_email).exists()
        username_exist = User.objects.filter(username=entered_username).exists()

        errors_list = []

        if len(entered_email)==0:
            raise serializers.ValidationError({"detail":"Falsche Anmeldedaten."})
       
        if email_exist:
            raise serializers.ValidationError({"email":"Diese E-Mail-Adresse wird bereits verwendet."})
        
        if username_exist:
            raise serializers.ValidationError({"username":"Diese Benutzername ist bereits vergeben."})

        if  not has_pwd_match:
             raise serializers.ValidationError({"password":"Das Passwort ist nicht gleich mit dem wiederholten Passwort."})
        return data

    
    def save(self):

        self.validated_data.pop('repeated_password')
        first_name = self.validated_data.pop('first_name', '')
        last_name = self.validated_data.pop('last_name', '')
        user_name = self.validated_data.pop('username','')
        type = self.validated_data.pop('type')

        if not user_name:
            user_name = self.validated_data['email']

        user = User(
            username=user_name,
            email=self.validated_data['email'],
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(self.validated_data['password'])
        user.save()
        Profile.objects.create(pk=user.pk ,user=user, type=type)
        return user
    
