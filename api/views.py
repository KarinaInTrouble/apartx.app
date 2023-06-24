from rest_framework import generics
from django.shortcuts import render
from web import models 
from .serializers import *
# Create your views here.

class OrdersList(generics.ListCreateAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = OrderSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer

class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
