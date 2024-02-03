
from django.urls import  path

from .views import *
from . import views

app_name = "viaje"

urlpatterns = [
    path('', index, name="index"),
    path("viaje/list/", ViajeCategoriaList.as_view(), name="viajecategoria_list"),
    path("viaje/form/", ViajeCategoriaCreate.as_view(), name="viajecategoria_form"),
    path("viaje/form_pais/", views.destino_form, name="viajecategoria_form2"),
    path("viaje/update/<int:pk>/", ViajeCategoriaUpdate.as_view(), name="viajecategoria_update"),
    path("viaje/delete/<int:pk>/", ViajeCategoriaDelete.as_view(), name="viajecategoria_confirm_delete"),
    path("viaje/detail/<int:pk>/", ViajeCategoriaDetail.as_view(), name="viajecategoria_detail"),
    

]
