from django import forms
from .models import Orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['user', 'order', 'price', 'description', 'address', 'route']