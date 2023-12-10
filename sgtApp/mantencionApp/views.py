from django.shortcuts import render, redirect, get_object_or_404
from mantencionApp.models import Mantenimiento
from mantencionApp.forms import MantenimientoForm

# Create your views here.

# MANTENCION
def mantencion(request):
    mantenimiento = Mantenimiento.objects.all()
    return render(request, 'seguimientoApp/mantencion.html', {'mantenimientos':mantenimiento})


def listar_mantencion(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'seguimientoApp/lista_mantencion.html', {'mantenimientos': mantenimientos})

def crear_mantencion(request):
    form = MantenimientoForm()
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mantencion')
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_mantencion.html', data)

def editar_mantencion(request, mantencion_id):
    mantenimiento = get_object_or_404(Mantenimiento, id=mantencion_id)
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_mantencion')
    else:
        form = MantenimientoForm(instance=mantenimiento)
    return render(request, 'seguimientoApp/editar_mantencion.html', {'form': form, 'mantenimientos': mantenimiento})

def eliminar_mantencion(request, mantencion_id):
    # Obtener el vehículo
    mantenimiento = Mantenimiento.objects.get(pk=mantencion_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        # notificaciones_asociadas = Notificacion.objects.filter(incidencia__mantencion=mantenimiento)
        # notificaciones_asociadas.delete()

        # Eliminar el vehículo
        mantenimiento.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('lista_mantencion')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_mantencion.html', {'mantenimientos': mantenimiento})