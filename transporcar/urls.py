"""transporcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reparaciones.views import lista_vehiculo, reparaciones
from personas.views import personas, vehiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-car/', lista_vehiculo),
    path('usuario/',personas),
    path('vehiculo/', vehiculo),
    path('lista_reparaciones/<id>', reparaciones),
]
