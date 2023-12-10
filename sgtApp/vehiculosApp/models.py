from django.db import models
from mantencionApp.models import Mantenimiento, Personal
from rastreoApp.models import Geolocalizacion


# Create your models here.

class TipoVehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'

    def __str__(self):
        return self.tipo_vehiculo
    
class Vehiculo(models.Model):
    numero_ppu = models.CharField(max_length=6, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    num_chasis = models.IntegerField(blank=True, null=True)
    ano_fabricacion = models.DateField(blank=True, null=True)
    kilometraje = models.FloatField(blank=True, null=True)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    tipo_vehiculo = models.ForeignKey(
        TipoVehiculo, models.DO_NOTHING, blank=True, null=True)
    geolocalizacion = models.ForeignKey(
        Geolocalizacion, models.DO_NOTHING, blank=True, null=True)
    mantenimiento = models.ForeignKey(
        Mantenimiento, models.DO_NOTHING, blank=True, null=True)
    personal = models.ForeignKey(
        Personal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'
    
    def __str__(self):
        return self.numero_ppu