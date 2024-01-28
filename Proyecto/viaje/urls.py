
from django.urls import  path

from .views import *

app_name = "viaje"

urlpatterns = [
    path('', index, name="index"),
    path("viaje/list/", ViajeCategoriaList.as_view(), name="viajecategoria_list"),
    path("viaje/form/", ViajeCategoriaCreate.as_view(), name="viajecategoria_form"),
     path("viaje/update/<int:pk>/", ViajeCategoriaUpdate.as_view(), name="viajecategoria_update"),
    path("viaje/delete/<int:pk>/", ViajeCategoriaDelete.as_view(), name="viajecategoria_delete"),
    path("viaje/detail/<int:pk>/", ViajeCategoriaDetail.as_view(), name="viajecategoria_detail"),
    

]
