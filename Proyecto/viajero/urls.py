
from django.urls import  path
from . import views

app_name = "viajero"

urlpatterns = [
    path('', views.index, name="index"),
    path('viajero/list', views.viajero_list, name="viajero_list"),
    path('viajero/form', views.viajero_form, name="viajero_form"),

]
