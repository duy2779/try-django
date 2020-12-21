from .models import Order


def cartTotal(request):
    total = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, status='C')
        total = order.get_cart_total

    return {'cartTotal': total}
