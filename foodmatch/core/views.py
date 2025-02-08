from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Donor, NGO, FoodItem, FoodRequest
from .serializers import DonorSerializer, NGOSerializer, FoodItemSerializer, FoodRequestSerializer

from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class NGOViewSet(viewsets.ModelViewSet):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodRequestViewSet(viewsets.ModelViewSet):
    queryset = FoodRequest.objects.all()
    serializer_class = FoodRequestSerializer
