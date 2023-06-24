from django import forms
from .models import *

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
    

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['message']
