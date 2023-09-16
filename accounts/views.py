from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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


def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
