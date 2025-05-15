
from models import Vuelo, Usuario,Empleado,Administrador, Pasajero,Pais,Ciudad,Reserva


class UsuarioService:
    @staticmethod
    def cargar_usuario(nombre, apellido, email, telefono,username):
        pasajero = Pasajero.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, username=username, estado=1)    
        return pasajero
    @staticmethod
    def cargar_empleado(nombre, apellido, email, telefono,username, salario, fecha):
        empleado = Empleado.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, username=username, estado=1, salario=salario, fecha=fecha)
        return empleado
    @staticmethod
    def editarPerfil(id,nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono, nuevoUsername):
        usuarioEncontrado = Usuario.objects.get(id=id)
        usuarioEncontrado.nombre = nuevoNombre
        usuarioEncontrado.apellido = nuevoApellido
        usuarioEncontrado.email = nuevoEmail
        usuarioEncontrado.telefono = nuevoTelefono
        usuarioEncontrado.username = nuevoUsername
        return usuarioEncontrado
    @staticmethod
    def cargar_administrador(nombre, apellido, email, telefono,username):
        administrador = Administrador.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, username=username, estado=1)
        return administrador
    @staticmethod
    def cerrar_sesion(id):
        usuarioEncontrado = Usuario.objects.get(id=id)
        usuarioEncontrado.estado = 0
    
class VueloService:
    @staticmethod
    def cargarVuelo(codigo, origen, destino, capacidad, fecha, hora_salida, hora_embarque):
        vuelo = Vuelo.objects.create(codigo=codigo, origen=origen, destino=destino, capacidad=capacidad, fecha=fecha, hora_salida=hora_salida, hora_embarque=hora_embarque)
        return vuelo
    @staticmethod
    def eliminar_vuelo(idVuelo):
        try:
            vuelo = Vuelo.objects.get(id=idVuelo)
            vuelo.delete()
            return f"Vuelo con ID {idVuelo} eliminado correctamente."
        except Vuelo.DoesNotExist:
            return "Vuelo no encontrado."
    @staticmethod
    def editar_vuelo(idVuelo, nuevoOrigen, nuevoDestino, nuevaCapacidad, nuevaFecha, nuevaHoraSalida, nuevaHoraEmbarque):
        vueloEncontrado = Vuelo.objects.get(id=idVuelo)
        if(vueloEncontrado != None):
            vueloEncontrado.origen = nuevoOrigen
            vueloEncontrado.destino = nuevoDestino
            vueloEncontrado.capacidad = nuevaCapacidad
            vueloEncontrado.fecha = nuevaFecha
            vueloEncontrado.hora_salida = nuevaHoraSalida
            vueloEncontrado.hora_embarque = nuevaHoraEmbarque
            vueloEncontrado.save()
            return "Vuelo modificado exitosamente"
        else:
            return "Vuelo no encontrado"

class EmpleadoService:
    @staticmethod
    def cargarVuelo(codigo, origen, destino, capacidad, fecha, hora_salida, hora_embarque):
        vuelo = Vuelo.objects.create(codigo=codigo, origen=origen, destino=destino, capacidad=capacidad, fecha=fecha, hora_salida=hora_salida, hora_embarque=hora_embarque)
        return vuelo
    @staticmethod
    def eliminar_vuelo(idVuelo):
        try:
            vuelo = Vuelo.objects.get(id=idVuelo)
            vuelo.delete()
            return f"Vuelo con ID {idVuelo} eliminado correctamente."
        except Vuelo.DoesNotExist:
            return "Vuelo no encontrado."
    @staticmethod
    def editar_vuelo(idVuelo, nuevoOrigen, nuevoDestino, nuevaCapacidad, nuevaFecha, nuevaHoraSalida, nuevaHoraEmbarque):
        vueloEncontrado = Vuelo.objects.get(id=idVuelo)
        if(vueloEncontrado != None):
            vueloEncontrado.origen = nuevoOrigen
            vueloEncontrado.destino = nuevoDestino
            vueloEncontrado.capacidad = nuevaCapacidad
            vueloEncontrado.fecha = nuevaFecha
            vueloEncontrado.hora_salida = nuevaHoraSalida
            vueloEncontrado.hora_embarque = nuevaHoraEmbarque
            vueloEncontrado.save()
            return "Vuelo modificado exitosamente"
        else:
            return "Vuelo no encontrado"
    @staticmethod
    def ver_usuarios():
        return Usuario.objects.all()
    @staticmethod
    def ver_reservas(vuelo):
        reservas = Reserva.objects.get(vuelo=vuelo)
        return reservas
    @staticmethod
    def buscar_pasajero(idPasajero):
        pasajeroEncontrado = Pasajero.objects.get(id=idPasajero)
        if pasajeroEncontrado != None:
            return pasajeroEncontrado
        else:
            return "Pasajero no encontrado"
    @staticmethod
    def ver_vuelos():
        vuelos = Vuelo.objects.all()
        return vuelos

class AdministradorService:
    @staticmethod
    def ver_empleados():
        empleados = Empleado.objects.all()
        return empleados
    @staticmethod
    def agregar_empleado(nombre, apellido, email, telefono, username):
        empleado = Empleado.objects.create(nombre=nombre,apellido=apellido,email=email, telefono=telefono, username=username, estado=1)
        return empleado
    @staticmethod
    def eliminar_empleado(idEmpleado):
        empleadoEliminar = Empleado.objects.get(id=idEmpleado)
        empleadoEliminar.delete()
    @staticmethod
    def editar_empleado(idEmpleado, nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono):
        empleadoEditar = Empleado.objects.get(id=idEmpleado)
        if(empleadoEditar != None):
            empleadoEditar.nombre = nuevoNombre
            empleadoEditar.apellido = nuevoApellido
            empleadoEditar.email = nuevoEmail
            empleadoEditar.telefono = nuevoTelefono
            empleadoEditar.save()
            return "Empleado modificado exitosamente"
        else:
            return "Empleado inexistente"
    @staticmethod
    def buscar_empleado(idEmpleado):
        empleadoEncontrado = Empleado.objects.get(id=idEmpleado)
        if(empleadoEncontrado != None):
            return empleadoEncontrado
        else:
            return "Sin resultados"

class PasajeroService:
    @staticmethod
    def crear_reserva(codigo, pasajero, vuelo, cantidad, fecha):
        reserva = Reserva.objects.create(codigo=codigo,pasajero=pasajero, vuelo=vuelo, cantidad=cantidad, fecha=fecha, estado='confirmado')
        return reserva
    @staticmethod
    def editar_reserva(idReserva,nuevoCodigo, nuevoPasajero, nuevoVuelo, nuevaCantidad, nuevaFecha):
        reservaObtenida = Reserva.objects.get(id=idReserva)
        if reservaObtenida != None:
            reservaObtenida.pasajero = nuevoPasajero
            reservaObtenida.vuelo = nuevoVuelo
            reservaObtenida.cantidad = nuevaCantidad
            reservaObtenida.fecha = nuevaFecha
            reservaObtenida.save()
        else:
            return "Reserva no encontrada"
    @staticmethod
    def eliminar_reserva(idReserva):
        reservaEliminar = Reserva.objects.get(id=idReserva)
        if reservaEliminar != None:
            reservaEliminar.delete()
    @staticmethod
    def buscar_reserva(idReserva):
        reservaEncontrada = Reserva.objects.get(id=idReserva)
        return reservaEncontrada
    @staticmethod
    def realizarCheckIn(idReserva):
        reservaEncontrada = Reserva.objects.get(id=idReserva)
        if reservaEncontrada != None:
            if reservaEncontrada.estado != 'checkin':
                reservaEncontrada.estado = 'checkin'
            else:
                return "Su reserva ya tiene hecho el check-in"
        else:
            return "Reserva inexistente"

