from django import forms

from .models import *

class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor
        fields = "__all__"
        widgets = {
            'id_asesor': forms.TextInput(attrs={'placeholder': 'Número de ID'}),
        }
   
        
