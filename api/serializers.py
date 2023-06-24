from rest_framework  import serializers
from web import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
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
