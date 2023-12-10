from django.db import models

# Create your models here.

class Mantenimiento(models.Model):
    tipo_mantenimiento = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    notas = models.CharField(max_length=60, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    personal = models.ForeignKey(
        'Personal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimiento'

class Personal(models.Model):
    rut = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_p = models.CharField(max_length=50, blank=True, null=True)
    apellido_m = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contraseña = models.CharField(max_length=50, blank=True, null=True)
    rol = models.ForeignKey('Rol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'
    
    def __str__(self):
        return self.nombre + " " + self.apellido_p
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    rut = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

class Repuesto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    proveedor = models.ForeignKey(
        Proveedor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repuesto'

class Rol(models.Model):
    cargo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'

class RptoMtto(models.Model):
    # The composite primary key (repuesto_id, mantenimiento_id) found, that is not supported. The first column is selected.
    repuesto = models.OneToOneField(
        Repuesto, models.DO_NOTHING, primary_key=True)
    mantenimiento = models.ForeignKey(Mantenimiento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rpto_mtto'
        unique_together = (('repuesto', 'mantenimiento'),)