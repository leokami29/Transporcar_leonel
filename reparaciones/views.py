from django.shortcuts import render
from reparaciones.models import Reparaciones, Vehiculo, Detalles
from vehiculos.models import Vehiculo

# Create your views here.
#Crear una lista para el listado de vehiculos
def lista_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculo':vehiculos}
    return render(request, 'lista_vehiculos.html', data)

def reparaciones(request, id):
    reparaciones = Reparaciones.objects.filter(vehiculo_id=id).last()
    detalle= Detalles.objects.filter(reparacion_id=reparaciones)
    total = 0
    for x in detalle:
        total = total+(x.costo * x.cantidad)
    data = {'reparaciones': reparaciones, 'detalle':detalle, 'total':total}
    return render(request, 'lista_reparaciones.html', data)

