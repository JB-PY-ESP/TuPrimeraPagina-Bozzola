from django.db import models


    
class Viajero(models.Model):
    nombre = models.CharField( max_length=100)
    apellido = models.CharField( max_length=100)
    email = models.EmailField(editable=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True, editable=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}" 
    
    class Meta:
        verbose_name = "viajero"
        verbose_name_plural = "viajeros"