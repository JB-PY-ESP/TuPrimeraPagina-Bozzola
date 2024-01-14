
from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asesor/list', views.asesor_list, name="asesor_list"),
    path('asesor/form', views.asesor_form, name="asesor_form"),
    path('viajero/list', views.viajero_list, name="viajero_list"),
    path('viajero/form', views.viajero_form, name="viajero_form"),
    path('viaje/list', views.viaje_list, name="viaje_list"),
    path('viaje/form', views.viaje_form, name="viaje_form"),

]
