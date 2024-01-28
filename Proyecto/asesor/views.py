from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import forms, models

def index(request):
    return render(request, "asesor/index.html")

def asesor_list(request):
    consulta = models.Asesor.objects.all()
    asesores_ordenados = sorted(consulta, key=lambda x: x.id_asesor)
    contexto = {"asesores": asesores_ordenados}
    return render(request, "asesor/asesor_list.html", contexto)

def asesor_form(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.AsesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asesor:asesor_list")
    else:
        form = forms.AsesorForm()
    
    return render(request, "asesor/asesor_form.html", {"form":form})
