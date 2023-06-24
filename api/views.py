from rest_framework import generics
from django.shortcuts import render
from web import models 
from .serializers import *
# Create your views here.

class ProfessionList(generics.ListCreateAPIView):
    queryset = models.Profession.objects.all()
    serializer_class = ProfessionSerializer

class DetailProfession(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profession.objects.all()
    serializer_class = ProfessionSerializer

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

class FeedbackList(generics.ListCreateAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = FeedbackSerializer

class DetailFeedback(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = FeedbackSerializer

class CompletedOrderList(generics.ListCreateAPIView):
    queryset = models.CompletedOrders.objects.all()
    serializer_class = CompletedOrderSerializer

class DetailCompletedOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CompletedOrders.objects.all()
    serializer_class = CompletedOrderSerializer

