from django.contrib import admin


from .models import *

admin.site.site_title = "Destinos"

class ViajeAdmin(admin.ModelAdmin):
    list_display = ("destino", "fecha_viaje", "viajero", "asesor", "comision", "fecha_actualizacion")
    list_display_links = ("viajero",)
    search_fields = ("viajero",)
    ordering = ("fecha_viaje", "destino")
    list_filter = ("destino",)
    date_hierarchy = "fecha_actualizacion"


admin.site.register(ViajeCategoria)
admin.site.register(Viaje, ViajeAdmin)



