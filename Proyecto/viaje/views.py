from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import *
from .models import *

def index(request):
    return render(request, "viaje/index.html")

class ViajeCategoriaList(ListView):
    model = ViajeCategoria
    # template_name = "producto/productocategoria_listXX.html"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = ViajeCategoria.objects.filter(pais__icontains=consulta)
        else:
            object_list = ViajeCategoria.objects.all()
        return object_list


class ViajeCategoriaCreate(CreateView):
    model = ViajeCategoria
    form_class = ViajeCategoriaForm
    success_url = reverse_lazy("viaje:viajecategoria_list")

class ViajeCategoriaUpdate( UpdateView):
    model = ViajeCategoria
    form_class = ViajeCategoriaForm2
    success_url = reverse_lazy("viaje:viajecategoria_list")


class ViajeCategoriaDelete(DeleteView):
    model = ViajeCategoria
    success_url = reverse_lazy("viaje:viajecategoria_list")
    

class ViajeCategoriaDetail(DetailView):
    model = ViajeCategoria

from django.http import HttpResponse

def destino_form(request) -> HttpResponse:
    if request.method == "POST":
        form = ViajeCategoriaForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viaje:viajecategoria_list")
    else:
        form = ViajeCategoriaForm2()
    
    return render(request, "viaje/viajecategoria_form2.html", {"form":form})