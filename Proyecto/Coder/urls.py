from django.contrib.auth.views import LogoutView
from django.urls import  path
from . import views
from .views import *

app_name = "Coder"

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="Coder/logout.html"), name="logout"),
    path("register/", register, name="register"),
]
