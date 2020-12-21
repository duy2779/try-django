from django.db import models
from products.models import Product
from customers.models import Customer

# Create your models here.


class Order(models.Model):
    cart = 'C'
    pending = 'P'
    outForDelivery = 'OFD'
    delivered = 'D'
    STATUS = [
        (cart, 'Cart'),
        (pending, 'Pending'),
        (outForDelivery, 'Out for delivery'),
        (delivered, 'Delivered'),
    ]
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(
        choices=STATUS, default=pending, null=False, max_length=200)

    @property
    def get_order_items(self):
        return self.orderitem_set.all()

    @property
    def get_cart_total(self):
        total = sum([item.quantity for item in self.get_order_items])
        return total

    @property
    def get_cart_amount(self):
        return sum([item.get_total for item in self.get_order_items])


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.DecimalField(
        default=0, decimal_places=0, max_digits=10, blank=True)

    def __str__(self):
        return self.product.title

    @property
    def get_total(self):
        return self.product.price * self.quantity
