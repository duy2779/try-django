from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {'title':'Home'}
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    context = {'title':'About'}
    return render(request, 'about.html', context)
