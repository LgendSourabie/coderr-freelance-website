
from django.utils.crypto import get_random_string
import random
from coderr_user_profile_app.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

def is_customer_guest(data):
    return data['username'] == "andrey" and data['password'] == "asdasd"

def is_business_guest(data):
    return data['username'] == "kevin" and data['password'] == "asdasd24"

def generate_guest_email():
    domains = [
        "test.com",
        "guest.com",
        "temp.com",
        "no-mail.com",
        "mock.com",
        "demo.com",
        "rnd-mail.com",
    ]

    random_domain = random.choice(domains)
    email = f"coderr-{get_random_string(6)}@{random_domain}" 
    return email

def generate_guest_username():
    names = [
        "Guest",
        "Demo",
        "Gast"
    ]

    random_name = random.choice(names)
    username = f"{random_name}-{get_random_string(6)}" 
    return username


def guest_login(request,profile_type):
        user = User.objects.create_user(
            username=generate_guest_username() ,
            email=generate_guest_email()
        )
        user.save()

        Profile.objects.create(pk=user.pk ,user=user, type=profile_type)

        login(request, user)

        token, _ = Token.objects.get_or_create(user=user)

        data = {
            "token": token.key,
            "email": user.email,
            "username": user.username,
            "user_id":user.id
        }
        return data
