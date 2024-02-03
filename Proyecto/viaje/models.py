from django.db import models
from django.utils import timezone
from asesor.models import Asesor
from viajero.models import Viajero
    
class ViajeCategoria(models.Model):
    pais = models.CharField(max_length=100) 
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return f"{self.pais}, {self.ciudad}"

    class Meta:
        verbose_name = "categoría de destino"
        verbose_name_plural = "categorías de destinos"
    
class Viaje(models.Model):
    destino = models.ForeignKey(ViajeCategoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_viaje = models.DateField(null=True, blank=True, editable=True)
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE,null=True, blank=True )
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True, blank=True )
    comision = models.FloatField()
    fecha_actualizacion = models.DateField(default=timezone.now, editable=False, verbose_name="fecha de actualización")
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    
    def __str__(self) -> str:
        return f"{self.fecha_viaje} - {self.viajero} - {self.destino}- Atendido por: {self.asesor}"
    
    class Meta:
        verbose_name = "viaje"
        verbose_name_plural = "viajes"