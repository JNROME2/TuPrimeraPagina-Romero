from django.db import models

class TiendaSucursales(models.Model):
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()

class TiendaClientes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()

class TiendaProductos(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    def __str__(self):
        return self.nombre

class TiendaInicio(models.Model):
    nombre = models.CharField(max_length=50)
   

