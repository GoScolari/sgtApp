
from django.db import models
from vehiculosApp.models import Vehiculo
from mantencionApp.models import Personal

# Create your models here.

class Incidencia(models.Model):
    fecha = models.DateField(blank=True, null=True)
    tipo_incidencia = models.CharField(max_length=50, blank=True, null=True)
    estado_incidencia = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidencia'

class Notificacion(models.Model):
    fecha = models.DateField(blank=True, null=True)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    incidencia = models.ForeignKey(
        Incidencia, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'

class NotfPers(models.Model):
    # The composite primary key (notificacion_id, personal_id) found, that is not supported. The first column is selected.
    notificacion = models.ForeignKey(
        Notificacion, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notf_pers'
        unique_together = (('notificacion', 'personal'),)
