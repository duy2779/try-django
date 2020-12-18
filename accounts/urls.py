from django.urls import path
from .views import login_view, register_view, log_out

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', log_out, name="logout"),
    path('register/', register_view, name="register"),
]
