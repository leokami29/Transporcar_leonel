from django.db import models
from vehiculos.models import Vehiculo

# from personas import models

# Create your models here.
class Reparaciones (models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=80)
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return str(self.fecha)+" "+str(self.costo)+" "+self.description
    
    
    
    
class Servicios (models.Model):
    description = models.CharField(max_length=80)
    perecio = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return str(self.description)+" "+str(self.perecio)
    
        
        
    
class Detalles (models.Model):
    costo = models.DecimalField(max_digits=15, decimal_places=0)
    cantidad = models.IntegerField(default=1)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE,null=True, blank=True)
    reparacion = models.ForeignKey(Reparaciones,on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return str(self.costo)+" "+str(self.cantidad)




    
    
    
    
    


