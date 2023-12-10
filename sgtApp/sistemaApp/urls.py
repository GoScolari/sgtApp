from django.urls import path
from .views import inicio_sesion, home, salir, panel

urlpatterns = [
    path('inicio-sesion/', inicio_sesion, name='inicio_sesion'),
    path('home/', home, name='home'),
    path('salir/', salir, name='salir'),
    path('panel/', panel, name='panel'),
    # Puedes agregar más rutas aquí según las vistas de sistemaApp
]

