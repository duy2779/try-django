from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import ProductForm
from .models import Product
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_user

# Create your views here.


@login_required(login_url='accounts:login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    productFilter = ProductFilter(request.GET, queryset=products)
    products = productFilter.qs

    context = {'title': 'Products', 'products': products,
               'productFilter': productFilter}
    return render(request, 'products/products.html', context)


@login_required(login_url='accounts:login')
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('products:products'))
    context = {'title': 'Create Product', 'form': form}
    return render(request, 'products/product_create.html', context)


@login_required(login_url='accounts:login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('products:products'))
    context = {'title': product.title.capitalize(), 'form': form}
    return render(request, 'products/product_create.html', context)


@login_required(login_url='accounts:login')
def product_switch_featured(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.featured = not product.featured
    product.save(update_fields=["featured"])
    return redirect(reverse('products:products'))


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)
