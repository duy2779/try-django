from django.urls import path
from .views import order_update

app_name = 'orders'

urlpatterns = [
    path('update/', order_update, name='order-update'),
]