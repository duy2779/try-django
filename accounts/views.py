from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('products:products'))
        else:
            messages.warning(request,'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:login'))
