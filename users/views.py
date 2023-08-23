from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserRegistrationSerializer


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer