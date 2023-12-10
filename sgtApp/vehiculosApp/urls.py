from django.urls import path
from .views import lista_vehiculos, detalle_vehiculo, gestionar_vehiculos, crear_vehiculo, editar_vehiculo, eliminar_vehiculo

app_name = 'vehiculosApp'

urlpatterns = [
    path('lista/', lista_vehiculos, name='lista_vehiculos'),
    path('detalle/<int:vehiculo_id>/', detalle_vehiculo, name='detalle_vehiculo'),
    path('gestionar/', gestionar_vehiculos, name='gestionar_vehiculos'),
    path('crear/', crear_vehiculo, name='crear_vehiculo'),
    path('editar/<int:vehiculo_id>/', editar_vehiculo, name='editar_vehiculo'),
    path('eliminar/<int:vehiculo_id>/', eliminar_vehiculo, name='eliminar_vehiculo'),
]
