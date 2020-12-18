from django.db import models
from products.models import Product
from customers.models import Customer

# Create your models here.
class Order(models.Model):
    pending = 'P'
    outForDelivery = 'OFD'
    delivered = 'D'
    STATUS = [
        (pending,'Pending'),
        (outForDelivery,'Out for delivery'),
        (delivered,'Delivered'),
    ]
    customer =models.ForeignKey(Customer, null=True, blank=True ,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=False, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=0)
    status = models.CharField(choices=STATUS, default=pending, null=False, max_length=200)