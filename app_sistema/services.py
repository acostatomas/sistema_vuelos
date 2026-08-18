
from .models import Vuelo, Usuario,Pais,Ciudad,Reserva,Empleado


class UsuarioService:
    @staticmethod
    def cargar_usuario(nombre, apellido, email, telefono, username, pasaporte=None):
        pasajero = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            username=username,
            estado=1,
            rol='PASAJERO',
            pasaporte=pasaporte
        )
        return pasajero

    @staticmethod
    def cargar_empleado(nombre, apellido, email, telefono, username, salario, fecha_ingreso, es_admin=False):
        empleado = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            username=username,
            estado=1,
            rol='ADMIN' if es_admin else 'EMPLEADO',
            salario=salario,
            fecha_ingreso=fecha_ingreso
        )
        return empleado

    @staticmethod
    def cargar_administrador(nombre, apellido, email, telefono, username, salario, fecha_ingreso):
        return UsuarioService.cargar_empleado(
            nombre, apellido, email, telefono, username, salario, fecha_ingreso, es_admin=True
        )

    @staticmethod
    def editarPerfil(id, nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono, nuevoUsername):
        try:
            usuarioEncontrado = Usuario.objects.get(id=id)
            usuarioEncontrado.nombre = nuevoNombre
            usuarioEncontrado.apellido = nuevoApellido
            usuarioEncontrado.email = nuevoEmail
            usuarioEncontrado.telefono = nuevoTelefono
            usuarioEncontrado.username = nuevoUsername
            usuarioEncontrado.save()
            return usuarioEncontrado
        except Usuario.DoesNotExist:
            return 'Usuario no encontrado'

    @staticmethod
    def cerrar_sesion(id):
        try:
            usuarioEncontrado = Usuario.objects.get(id=id)
            usuarioEncontrado.estado = 0
            usuarioEncontrado.save()
            return usuarioEncontrado
        except Usuario.DoesNotExist:
            return 'Usuario no encontrado'
    
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
            return True
        except Vuelo.DoesNotExist:
            return False
    @staticmethod
    def buscar_vuelo(idVuelo):
        vueloEncontrado = Vuelo.objects.get(id=idVuelo)
        if(vueloEncontrado != None):
            return vueloEncontrado
        else:
            return None
    @staticmethod
    def buscar_vuelo_por_codigo(codigo):
        vueloEncontrado = Vuelo.objects.filter(codigo=codigo).first()
        if(vueloEncontrado != None):
            return vueloEncontrado
        else:
            return None
    @staticmethod
    def editar_vuelo(idVuelo, nuevoOrigen, nuevoDestino, nuevaCapacidad, nuevaFecha, nuevaHoraSalida, nuevaHoraEmbarque):
        vueloEncontrado = Vuelo.objects.get(codigo=idVuelo)
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
        vuelo = Vuelo.objects.create(
            codigo=codigo,
            origen=origen,
            destino=destino,
            capacidad=capacidad,
            fecha=fecha,
            hora_salida=hora_salida,
            hora_embarque=hora_embarque
        )
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
        try:
            vueloEncontrado = Vuelo.objects.get(id=idVuelo)
            vueloEncontrado.origen = nuevoOrigen
            vueloEncontrado.destino = nuevoDestino
            vueloEncontrado.capacidad = nuevaCapacidad
            vueloEncontrado.fecha = nuevaFecha
            vueloEncontrado.hora_salida = nuevaHoraSalida
            vueloEncontrado.hora_embarque = nuevaHoraEmbarque
            vueloEncontrado.save()
            return "Vuelo modificado exitosamente"
        except Vuelo.DoesNotExist:
            return "Vuelo no encontrado"

    @staticmethod
    def ver_usuarios():
        return Usuario.objects.all()

    @staticmethod
    def ver_reservas(vuelo):
        return Reserva.objects.filter(vuelo=vuelo)

    @staticmethod
    def buscar_pasajero(idPasajero):
        try:
            pasajeroEncontrado = Usuario.objects.get(id=idPasajero)
            return pasajeroEncontrado
        except Usuario.DoesNotExist:
            return "Pasajero no encontrado"

    @staticmethod
    def ver_vuelos():
        return Vuelo.objects.all()

class AdministradorService:
    @staticmethod
    def ver_empleados():
        empleados = Empleado.objects.all()
        return empleados
    @staticmethod
    def agregar_empleado(nombre, apellido, email, telefono, salario,fecha_ingreso):
        empleado = Empleado.objects.create(nombre=nombre,apellido=apellido,email=email, telefono=telefono, salario=salario,fecha_ingreso=fecha_ingreso)
        return empleado
    @staticmethod
    def eliminar_empleado(idEmpleado):
        try:
            empleadoEliminar = Empleado.objects.get(id=idEmpleado)
            empleadoEliminar.delete()
            return "Empleado eliminado correctamente"
        except Usuario.DoesNotExist:
            return "Empleado a eliminar inexistente"
    @staticmethod
    def editar_empleado(idEmpleado, nuevoNombre, nuevoApellido, nuevoEmail, nuevoTelefono, nuevoSalario):
        try:
            empleadoEditar = Empleado.objects.get(id=idEmpleado)
            empleadoEditar.nombre = nuevoNombre
            empleadoEditar.apellido = nuevoApellido
            empleadoEditar.email = nuevoEmail
            empleadoEditar.telefono = nuevoTelefono
            empleadoEditar.salario = nuevoSalario
            empleadoEditar.save()
            return "Empleado modificado exitosamente"
        except Usuario.DoesNotExist:
            return "Empleado inexistente"
    @staticmethod
    def buscar_empleado(idEmpleado):
        empleado = Empleado.objects.filter(id=idEmpleado).first()
        if empleado != None:
            return empleado
        else:
            return None

class PasajeroService:
    @staticmethod
    def crear_reserva( pasajero, vuelo, cantidad, fecha):
        return Reserva.objects.create(
            pasajero=pasajero,
            vuelo=vuelo,
            cantidad=cantidad,
            fecha=fecha,
            estado='confirmado'
        )

    @staticmethod
    def editar_reserva(idReserva, nuevoCodigo, nuevoPasajero, nuevoVuelo, nuevaCantidad, nuevaFecha):
        try:
            reservaObtenida = Reserva.objects.get(id=idReserva)
            reservaObtenida.pasajero = nuevoPasajero
            reservaObtenida.vuelo = nuevoVuelo
            reservaObtenida.cantidad = nuevaCantidad
            reservaObtenida.fecha = nuevaFecha
            reservaObtenida.save()
            return "Reserva modificada exitosamente"
        except Reserva.DoesNotExist:
            return "Reserva no encontrada"

    @staticmethod
    def eliminar_reserva(idReserva):
        reservaEliminar = Reserva.objects.filter(id=idReserva)
        if reservaEliminar.exists():
            reservaEliminar.delete()
            return "Reserva eliminada correctamente"
        else:
            return "Reserva no encontrada"

    @staticmethod
    def buscar_reserva(idReserva):
        try:
            return Reserva.objects.get(id=idReserva)
        except Reserva.DoesNotExist:
            return "Reserva no encontrada"

    @staticmethod
    def realizarCheckIn(idReserva):
        try:
            reservaEncontrada = Reserva.objects.get(id=idReserva)
            if reservaEncontrada.estado != 'checkin':
                reservaEncontrada.estado = 'checkin'
                reservaEncontrada.save()
                return "Check-in realizado correctamente"
            else:
                return "Su reserva ya tiene hecho el check-in"
        except Reserva.DoesNotExist:
            return "Reserva inexistente"
