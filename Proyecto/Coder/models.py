from django.db import models

class Asesor(models.Model):
    nombre = models.CharField( max_length=100)  
    apellido = models.CharField( max_length=100) 
    email = models.EmailField()
    id_asesor = models.PositiveBigIntegerField()    
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Viajero(models.Model):
    nombre = models.CharField( max_length=100)
    apellido = models.CharField( max_length=100)
    email = models.EmailField(editable=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True, editable=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}" 
    
class Viaje(models.Model):
    pais = models.CharField( max_length=100)
    ciudad = models.CharField( max_length=100)
    fecha_viaje = models.DateField(null=True, blank=True, editable=True)
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE,null=True, blank=True )
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True, blank=True )
    
    def __str__(self) -> str:
        return f"{self.fecha_viaje} - {self.viajero} - {self.ciudad},{self.pais} - Atendido por: {self.asesor}"
    