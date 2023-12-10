from django.shortcuts import render
from vehiculosApp.models import Vehiculo



# Create your views here.

def rastreo (request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/rastreo.html', {'vehiculos': vehiculos})