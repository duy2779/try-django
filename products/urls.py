
from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    #admin
    path('', products, name='products'),
    path('create/', product_create, name='product-create'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('featured/<int:pk>/', product_switch_featured, name='product-switch-featured'),

    #user
    path('all/', all_products, name='all-products'),
]