from django.db import models 
from services import VueloService,UsuarioService,AdministradorService,EmpleadoService,PasajeroService
# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre}, {self.pais.nombre}"
    def getpais(self):
        return f"{self.pais.nombre}"
class Vuelo(models.Model):
    codigo = models.CharField(unique=True,max_length=5)
    origen = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='ciudad_origen')
    destino = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='ciudad_destino')
    capacidad = models.IntegerField()
    fecha = models.DateField()
    hora_salida = models.TimeField()
    hora_embarque = models.TimeField()
    def capacidadLlena(self,cantActualPasajeros):
        return cantActualPasajeros >= self.capacidad
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    estado = models.IntegerField(choices=[(0,'no disponible'),(1,'disponible')])
    def cargar_usuario(self,nombre, apellido, email, telefono,username):
        UsuarioService.cargar_usuario(nombre, apellido, email, telefono,username)
    def editarPerfil(self,nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono, nuevoUsername):
        UsuarioService.editarPerfil(self.id,nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono, nuevoUsername)
    def cerrarSesion(self):
        UsuarioService.cerrar_sesion(self.id)
    
class Pasajero(Usuario):
    pasaporte = models.CharField(max_length=10, unique=True)
    def crear_reserva(self, codigo, pasajero, vuelo, cantidad, fecha):
        PasajeroService.crear_reserva(codigo, pasajero, vuelo, cantidad, fecha)
    def editar_reserva(self,idReserva,nuevoCodigo, nuevoPasajero, nuevoVuelo, nuevaCantidad, nuevaFecha):
        PasajeroService.editar_reserva(idReserva,nuevoCodigo, nuevoPasajero, nuevoVuelo, nuevaCantidad, nuevaFecha)
    def eliminar_reserva(self, idReserva):
        PasajeroService.eliminar_reserva(idReserva)
    def buscar_reserva(self, idReserva):
        PasajeroService.buscar_reserva(idReserva)
    def realizarCheckIn(self, idReserva):
        PasajeroService.realizarCheckIn(idReserva)


class Empleado(Usuario):
    salario = models.IntegerField()
    fecha_ingreso = models.DateField()
    def cargarVuelo(self, codigo, origen, destino, capacidad, fecha, hora_salida, hora_embarque):
        Empleado.cargarVuelo(codigo, origen, destino, capacidad, fecha, hora_salida, hora_embarque)
    def eliminar_vuelo(self, idVuelo):
        Empleado.eliminar_vuelo(idVuelo)
    def editar_vuelo(self, idVuelo, nuevoOrigen, nuevoDestino, nuevaCapacidad, nuevaFecha, nuevaHoraSalida, nuevaHoraEmbarque):
        EmpleadoService.editar_vuelo(idVuelo, nuevoOrigen, nuevoDestino, nuevaCapacidad, nuevaFecha, nuevaHoraSalida, nuevaHoraEmbarque)
    def ver_usuarios(self):
        EmpleadoService.ver_usuarios()
    def ver_reservas(self, vuelo):
        EmpleadoService.ver_reservas()
    def buscar_pasajero(self, idPasajero):
        EmpleadoService.buscar_pasajero(idPasajero)
    def ver_vuelos(self):
        EmpleadoService.ver_vuelos()

    
class Administrador(Empleado):
    def ver_empleados(self):
        AdministradorService.ver_empleados()
    def agregar_empleado(self, nombre, apellido, email, telefono, username):
        AdministradorService.agregar_empleado(nombre, apellido, email, telefono, username)
    def eliminar_empleado(self,idEmpleado):
        AdministradorService.eliminar_empleado(idEmpleado)
    def editar_empleado(self,idEmpleado, nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono):
        AdministradorService.editar_empleado(idEmpleado, nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono)
    def buscar_empleado(self,idEmpleado):
        AdministradorService.buscar_empleado(idEmpleado)


class Reserva(models.Model):
    codigo = models.CharField(unique=True,max_length=7)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='reservas')
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    estado = models.CharField(choices=[('confirmado','Confirmado'),('checkin','Check-In'),('cancelado','Cancelado')], max_length=10)
    def getEstado(self):
        return self.estado
    