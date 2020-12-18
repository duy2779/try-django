from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=100000000)
    description = models.TextField(max_length=1000)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.pk})

    def get_switch_featured(self):
        return reverse("products:product-switch-featured", kwargs={"pk": self.pk})
