from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders')
    else:
        form = OrdersForm()
    return render(request, 'create_order.html', {'form': form})