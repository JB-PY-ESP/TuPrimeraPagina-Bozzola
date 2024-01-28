from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import forms, models

def index(request):
    return render(request, "viajero/index.html")

def viajero_list(request):
    consulta = models.Viajero.objects.all()
    viajeros_ordenados = sorted(consulta, key=lambda x: x.apellido)
    contexto = {"viajeros": viajeros_ordenados}
    return render(request, "viajero/viajero_list.html", contexto)

def viajero_form(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.ViajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viajero:viajero_list")
    else:
        form = forms.ViajeroForm()
    
    return render(request, "viajero/viajero_form.html", {"form":form})
    
