from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre}, {self.pais.nombre}"
class Vuelo(models.Model):
    codigo = models.CharField(unique=True,max_length=10)
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    fecha = models.DateField()
    hora_salida = models.TimeField()
    hora_embarque = models.TimeField()
    def capacidadLlena(self,cantActualPasajeros):
        return cantActualPasajeros >= self.capacidad
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #nombre = models.CharField(max_length=100)
    #apellido = models.CharField(max_length=100)
    #email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    #username = models.CharField(max_length=100)
    estado = models.IntegerField(choices=[(0,'no disponible'),(1,'disponible')])
    pasaporte = models.CharField(max_length=10, blank=True, null=True, unique=True)
    salario = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
   

class Reserva(models.Model):
    #codigo = models.CharField(unique=True,max_length=7)
    pasajero = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    estado = models.CharField(choices=[('confirmado','Confirmado'),('checkin','Check-In'),('cancelado','Cancelado')], max_length=10)
    

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    salario = models.IntegerField()
    fecha_ingreso = models.DateField()