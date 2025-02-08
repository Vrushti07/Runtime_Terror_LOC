# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    food_needed = models.CharField(max_length=255)

class FoodItem(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    pickup_location = models.CharField(max_length=255)
    status = models.CharField(choices=[("Available", "Available"), ("Claimed", "Claimed")], max_length=10)

class FoodRequest(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Rejected", "Rejected")], max_length=10)
