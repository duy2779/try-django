from django.urls import path
from .views import profile_view, orders_view

app_name = 'customers'

urlpatterns = [
    path('',  profile_view, name='profile-view'),
    path('orders/',  orders_view, name='orders-view'),
]