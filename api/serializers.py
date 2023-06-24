from rest_framework  import serializers
from web import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'avatar',
            'profession',
            'bio',
            'document',
        )
        model = models.Profile

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'order',
            'price',
            'description',
            'date',
            'address',
            'route_link',
            'route',
            'contract'
        )
        model = models.Orders

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'order',
            'user',
            'personal',
            'rate',
            'comment',
        )
        model = models.Feedback

class CompletedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'order',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'comment',
            'rate'
        )
        model = models.CompletedOrders

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'order',
            'user',
            'message',
            'is_accepted',
        )
        model = models.Response


