
from django.urls import  path
from . import views

app_name = "asesor"

urlpatterns = [
    path('', views.index, name="index"),
    path('asesor/list/', views.asesor_list, name="asesor_list"),
    path('asesor/form/', views.asesor_form, name="asesor_form"),

]
