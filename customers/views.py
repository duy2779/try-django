from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Customer
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_user
from .forms import CustomerForm

# Create your views here.


@login_required(login_url='accounts:login')
@allowed_user(allowed_roles=['customer'])
def profile_view(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(reverse('customers:profile-view'))
    context = {'customer': customer, 'form':form, 'title':'Profile customer'}
    return render(request, 'customers/profile.html', context)


@login_required(login_url='accounts:login')
@allowed_user(allowed_roles=['customer'])
def orders_view(request):
    customer = get_object_or_404(Customer, user=request.user)
    orders = customer.order_set.all()
    print(orders)
    context = {'customer': customer, 'orders': orders}
    return render(request, 'customers/orders.html', context)
