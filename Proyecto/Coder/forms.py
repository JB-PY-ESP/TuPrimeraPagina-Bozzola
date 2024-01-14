from django import forms

from . import models

class AsesorForm(forms.ModelForm):
    class Meta:
        model = models.Asesor
        fields = "__all__"
        widgets = {
            'id_asesor': forms.TextInput(attrs={'placeholder': 'Número de ID'}),
        }
        
class ViajeroForm(forms.ModelForm):
    class Meta:
        model = models.Viajero
        fields = "__all__"
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'})
        }        
        
class ViajeForm(forms.ModelForm):
    class Meta:
        model = models.Viaje
        fields = "__all__"
        widgets = {
            'fecha_viaje': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'}),
        }


        
