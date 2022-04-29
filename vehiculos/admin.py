from django.contrib import admin
from vehiculos.models import Vehiculo, Infraccion

# Register your models here.
class VehiculoAdmin (admin.ModelAdmin):
    list_display = ('placa','modelo','marca','Capacidad')
    list_filter = ('marca', 'modelo',)
    search_fields = ('placa','marca',)
    
admin.site.register(Vehiculo, VehiculoAdmin)


class InfraccionAdmin (admin.ModelAdmin):
    list_display = ('fecha','description','valor')
    list_filter = ('fecha',)
    search_fields = ('fecha','description',)
    
admin.site.register(Infraccion, InfraccionAdmin)




