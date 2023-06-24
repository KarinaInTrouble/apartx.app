from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def orders(request):
    query = Orders.objects.all()
    return render(request, 'orders.html', {'query': query})

def order_detail(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    responses = order.responses.all()

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.order = order
            response.user = request.user
            response.save()
            return redirect('order_detail', order_id=order_id)
    else:
        form = ResponseForm()

    return render(request, 'order_detail.html', {'order': order, 'responses': responses, 'form': form})

def response_status(request, order_id, response_id):
    response = get_object_or_404(Response, pk=response_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'accept':
            response.is_accepted = True
        elif status == 'reject':
            response.is_accepted = False
        response.save()
        return redirect('order_detail', order_id=order_id)
    return render(request, 'response_status.html', {'response': response})