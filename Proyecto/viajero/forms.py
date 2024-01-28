from django import forms

from .models import *

class ViajeroForm(forms.ModelForm):
    class Meta:
        model = Viajero
        fields = "__all__"
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'})
        }        



        
