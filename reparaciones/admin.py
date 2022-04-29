from django.contrib import admin
from reparaciones.models import Reparaciones, Servicios, Detalles

# Register your models here.
# class ReparacionesAdmin (admin.ModelAdmin):
#     list_display = ('fecha','costo','description')
#     list_filter = ('fecha', 'costo',)
#     search_fields = ('fecha','description',)
    
# admin.site.register(Reparaciones, ReparacionesAdmin)


class DetallesAdmin (admin.ModelAdmin):
    list_display = ('costo','servicio')
    list_filter = ('servicio',)
    search_fields = ('costo','servicio',)
    
admin.site.register(Detalles, DetallesAdmin)


class ServiciosAdmin (admin.ModelAdmin):
    list_display = ('perecio','description')
    list_filter = ('perecio','description',)
    search_fields = ('perecio','description',)
    
admin.site.register(Servicios, ServiciosAdmin)



#para que salga el formulario maestro detalle
#
class detalle_Reparaciones(admin.TabularInline):
    model=Detalles
    
class ReparacionesAdmin(admin.ModelAdmin):
    list_display = ('fecha','costo','description','vehiculo')
    list_filter = ('fecha', 'costo',)
    search_fields = ('fecha','description',)
    inlines=(detalle_Reparaciones,)
    
admin.site.register(Reparaciones, ReparacionesAdmin)
