from django.contrib import admin
from django.urls import path, include
from sistemaApp.urls import urlpatterns as sistemaApp_urls
from sistemaApp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('sistemaApp/', include('sistemaApp.urls')),
]

