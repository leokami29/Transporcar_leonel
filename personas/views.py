from django.shortcuts import render

from django.http import HttpResponse
from personas.models import Usuario
from vehiculos.models import Vehiculo
# Create your views here.
def index(request):
     return render(request,'home.html')

def personas(request):
    usuario = Usuario.objects.all()
    data = {'usuario': usuario}
    return render(request, 'listado_usuario.html', data)

def vehiculo(request):
     idusuario = request.POST.get('id')
     usuario= Usuario.objects.all()
     vehiculos = Vehiculo.objects.filter(usuario=idusuario)
     data = {'vehiculos': vehiculos, 'id':idusuario, 'usuario':usuario}
     return render(request, 'listado_usuario.html', data)

