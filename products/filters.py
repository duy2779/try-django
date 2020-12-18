import django_filters
from django import forms
from .models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains',label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Key word'}))
    class Meta:
        model = Product
        fields = ['title']
