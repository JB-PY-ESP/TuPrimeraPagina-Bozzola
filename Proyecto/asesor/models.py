from django.db import models

class Asesor(models.Model):
    nombre = models.CharField( max_length=100)  
    apellido = models.CharField( max_length=100) 
    email = models.EmailField()
    id_asesor = models.PositiveBigIntegerField()    
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "asesor"
        verbose_name_plural = "asesores"