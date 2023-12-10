from django.urls import path
from .views import mantencion, listar_mantencion, crear_mantencion, editar_mantencion, eliminar_mantencion

app_name = 'mantencionApp'

urlpatterns = [
    path('mantencion/', mantencion, name='mantencion_incidencias'),
    path('lista/', listar_mantencion, name='lista_mantencion_incidencias'),
    path('crear/', crear_mantencion, name='crear_mantencion_incidencias'),
    path('editar/<int:mantencion_id>/', editar_mantencion, name='editar_mantencion_incidencias'),
    path('eliminar/<int:mantencion_id>/', eliminar_mantencion, name='eliminar_mantencion_incidencias'),
]
