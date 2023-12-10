from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from vehiculosApp.models import Vehiculo

# Create your views here.

# LOGIN
def inicio_sesion (request):
    return render(request, 'registration/login.html')
@login_required
def home (request):
    return render(request, 'seguimientoApp/index.html')


def salir (request):
    logout(request)
    return redirect('/')

def panel(request):
    vehiculos = Vehiculo.objects.all()
    # Puedes agregar lógica adicional aquí para obtener datos de otras secciones como mantenimientos y personal
    
    return render(request, 'seguimientoApp/panel.html', {'vehiculos': vehiculos})
