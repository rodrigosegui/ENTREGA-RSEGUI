from django.db import models

# Create your models here.
class Huesped(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()


class Alojamientos(models.Model):

    nombreA = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    habitaciones = models.IntegerField()
    precioxdia = models.FloatField()


class Vehiculos(models.Model):

    nombreV = models.CharField(max_length=40)
    asientos = models.IntegerField()
    preciodiario = models.FloatField()