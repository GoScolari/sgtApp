from django.shortcuts import render, redirect, get_object_or_404
from incidenciasApp.models import Incidencia
from incidenciasApp.forms import IncidenciaForm

# Create your views here.


# INCIDENCIAS
def lista_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'seguimientoApp/lista_incidencias.html', {'incidencias': incidencias})

def detalle_incidencia(request, incidencia_id):

    incidencia = get_object_or_404(Incidencia, pk=incidencia_id)
    return render(request, 'seguimientoApp/detalle_incidencia.html', {'incidencia': incidencia})

def gestionar_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'seguimientoApp/gestionar_incidencias.html', {'incidencias': incidencias})

def crear_incidencia(request):
    form = IncidenciaForm()
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')  # Reemplaza con el nombre correcto de la URL
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_incidencia.html', data)

def editar_incidencia(request, incidencia_id):
    incidencia = get_object_or_404(Incidencia, id=incidencia_id)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')
    else:
        form = IncidenciaForm(instance=incidencia)
    return render(request, 'seguimientoApp/editar_incidencia.html', {'form': form, 'incidencia': incidencia})

def eliminar_incidencia(request, incidencia_id):
    incidencia = Incidencia.objects.get(pk=incidencia_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        # notificaciones_asociadas = Notificacion.objects.filter(vehiculo=incidencia.vehiculo)
        # notificaciones_asociadas.delete()

        # Eliminar el vehículo
        incidencia.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('gestionar_incidencias')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_incidencia.html', {'incidencia': incidencia})