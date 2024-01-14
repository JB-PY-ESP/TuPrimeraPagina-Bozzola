from django.shortcuts import redirect, render
from . import models
from . import forms

def index(request):
    return render(request, "Coder/index.html")

def asesor_list(request):
    consulta = models.Asesor.objects.all()
    asesores_ordenados = sorted(consulta, key=lambda x: x.id_asesor)
    contexto = {"asesores": asesores_ordenados}
    return render(request, "Coder/asesor_list.html", contexto)

def asesor_form(request):
    if request.method == "POST":
        form = forms.AsesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asesor_list")
    else:
        form = forms.AsesorForm()
    
    return render(request, "Coder/asesor_form.html", {"form":form})

def viajero_list(request):
    consulta = models.Viajero.objects.all()
    viajeros_ordenados = sorted(consulta, key=lambda x: x.apellido)
    contexto = {"viajeros": viajeros_ordenados}
    return render(request, "Coder/viajero_list.html", contexto)

def viajero_form(request):
    if request.method == "POST":
        form = forms.ViajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viajero_list")
    else:
        form = forms.ViajeroForm()
    
    return render(request, "Coder/viajero_form.html", {"form":form})
    

def viaje_list(request):
    consulta = models.Viaje.objects.all().order_by('fecha_viaje')
    contexto = {"viajes": consulta}
    return render(request, "Coder/viaje_list.html", contexto)

def viaje_form(request):
    if request.method == "POST":
        form = forms.ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viaje_list")
    else:
        form = forms.ViajeForm()
    
    return render(request, "Coder/viaje_form.html", {"form":form})

