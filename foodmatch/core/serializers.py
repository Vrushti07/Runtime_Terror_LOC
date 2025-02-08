from rest_framework import serializers
from .models import Donor, NGO, FoodItem, FoodRequest

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donor, NGO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        username = serializers.CharField(write_only=True)
        password = serializers.CharField(write_only=True)

    class Meta:
        model = Donor
        fields = ['id', 'username', 'password', 'name', 'location', 'contact']

    def create(self, validated_data):
        # Extract user-related fields
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        # Create a new User
        user = User.objects.create_user(username=username, password=password)

        # Create a Donor linked to this User
        donor = Donor.objects.create(user=user, **validated_data)
        return donor

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class FoodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = '__all__'
