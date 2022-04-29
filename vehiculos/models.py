from django.db import models
from personas.models import Conductor, Usuario

# from personas import models

# Create your models here.
class Vehiculo (models.Model):
   placa = models.CharField(max_length=10)
   modelo = models.IntegerField(default=2021)
   marca = models.CharField(max_length=30)
   Capacidad = models.IntegerField(default=1)
   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
   conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, null=True, blank=True)
  
   def __str__(self):
        return " "+ self.placa+" "+str(self.modelo)+" "+self.marca
    
    
    

class Infraccion (models.Model):
   fecha = models.DateField()
   description = models.CharField(max_length=30)
   valor = models.IntegerField(default=1)
   vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
   conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, null=True, blank=True)
  
   def __str__(self):
        return self.fecha+" "+self.description+" "+str(self.valor)
    
    
    


