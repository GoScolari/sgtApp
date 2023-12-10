from django.shortcuts import render, redirect, get_object_or_404
from vehiculosApp.models import Vehiculo
from incidenciasApp.models import Notificacion
from vehiculosApp.forms import VehiculoForm

# Create your views here.

# VEHICULOS
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/lista_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    return render(request, 'seguimientoApp/detalle_vehiculo.html', {'vehiculo': vehiculo})

def home(request):
    vehiculos = Vehiculo.objects.all()  # Asegúrate de importar el modelo Vehiculo
    return render(request, 'seguimientoApp/index.html', {'vehiculos': vehiculos})

def gestionar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/gestionar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_vehiculo.html', data)

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'seguimientoApp/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

def eliminar_vehiculo(request, vehiculo_id):
    # Obtener el vehículo
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        notificaciones_asociadas = Notificacion.objects.filter(incidencia__vehiculo=vehiculo)
        notificaciones_asociadas.delete()

        # Eliminar el vehículo
        vehiculo.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('gestionar_vehiculos')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_vehiculo.html', {'vehiculo': vehiculo})