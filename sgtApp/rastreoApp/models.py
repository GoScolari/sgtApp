from django.db import models

# Create your models here.

class Geolocalizacion(models.Model):
    geolocalizacion = models.CharField(max_length=50, blank=True, null=True)
    velocidad = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geolocalizacion'