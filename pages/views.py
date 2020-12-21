from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {'title': 'Home'}
    return render(request, 'home.html', context)


def about_view(request, *args, **kwargs):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


@login_required(login_url='accounts:login')
def cart_view(request, *args, **kwargs):
    customer = request.user.customer
    cart, created = Order.objects.get_or_create(customer=customer, status='C')
    cartItems = cart.orderitem_set.all()
    context = {'cartItems': cartItems, 'amount':cart.get_cart_amount}
    return render(request, 'cart.html', context)
