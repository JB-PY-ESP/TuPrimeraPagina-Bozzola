from django import forms

from . import models

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del profesor'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email del profesor'}),
        }
        