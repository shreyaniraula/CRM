from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_order = order.count()
    orders_delivered = order.filter(status='Delivered').count()
    orders_pending = order.filter(status='Pending').count()
    
    context = {'customer': customer, 'order': order,
    'total_order': total_order, 'orders_delivered': orders_delivered,
    'orders_pending': orders_pending
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products.html', {'product': product})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()

    context = {'customer': customer, 'order': order}
    return render(request, 'accounts/customer.html', context)
