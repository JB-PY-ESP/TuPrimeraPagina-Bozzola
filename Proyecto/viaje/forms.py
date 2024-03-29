from django import forms

from .models import *


class ViajeCategoriaForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = "__all__"
        widgets = {
            'fecha_viaje': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'}),
        }
        
class ViajeCategoriaForm2(forms.ModelForm):
    class Meta:
        model = ViajeCategoria
        fields = ['pais','ciudad','descripcion']

