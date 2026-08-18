from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.http import Http404
from .models import Reserva,Vuelo,Empleado
from .models import Usuario
from django.shortcuts import redirect
from django.contrib import messages
from .forms import VueloForm, RegistroForm, ReservaForm, VueloEditarForm, VueloBuscarForm,UsuarioEditarForm,EmpleadoForm,EmpleadoBuscarForm,EmpleadoEditarForm
from .services import VueloService, EmpleadoService, PasajeroService, AdministradorService
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from datetime import date

#VISTA DE INICIO: DEPENDIENDO DEL ROL DEL USUARIO, LO REDIRIGE A UN TEMPLATE DISTINTO
@login_required
def index(request):
    user = request.user

    if user.groups.filter(name='ADMINISTRADOR').exists():
        template = 'index.html'
    elif user.groups.filter(name='EMPLEADO').exists():
        template = 'index-empleado.html'
    elif user.groups.filter(name='PASAJERO').exists():
        #template = 'index-pasajero.html'
        return listar_vuelos_pasajero_con_filtro(request)
    else:
        return HttpResponseForbidden("No tenés permiso para ver esta página.")

    context = {
        'title': 'Gestión de Vuelos',
        '': ''
    }

    return render(request, template, context)

#SOBRE VUELOS
#CREAR VUELO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR']).exists())
def crear_vuelo(request):
    if request.method == 'POST':
        formulario = VueloForm(request.POST)
        if formulario.is_valid():
            VueloService.cargarVuelo(
                formulario.cleaned_data['codigo'],
                formulario.cleaned_data['origen'],
                formulario.cleaned_data['destino'],
                formulario.cleaned_data['capacidad'],
                formulario.cleaned_data['fecha'],
                formulario.cleaned_data['hora_salida'],
                formulario.cleaned_data['hora_embarque']
            )
            return redirect('inicio')
    else:
        formulario = VueloForm()
    return render(request,'nuevoVuelo.html',{'form':formulario})


#EDITAR VUELO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR']).exists())
def editar_vuelo(request, vuelo_id):
    vuelo = VueloService.buscar_vuelo(vuelo_id)
    if vuelo is None:
        raise Http404("No encontrado")
    if request.method == 'POST':
        formulario = VueloEditarForm(request.POST,instance=vuelo)
        if formulario.is_valid():
            formulario.save()
            #vuelo.codigo = formulario.cleaned_data['codigo']
            return redirect('vuelos')  # o donde quieras redirigir
    else:
        formulario = VueloEditarForm(instance=vuelo)

    return render(request, 'formulario-editar-vuelo.html', {'form': formulario})

#ELIMINAR VUELO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR']).exists())
def eliminar_vuelo(request,vuelo_id):
    vuelo = VueloService.eliminar_vuelo(vuelo_id)
    if vuelo:
        messages.success(request,"Vuelo eliminado correctamente")
    else:
        raise Http404("Vuelo a eliminar no encontrado")
    return redirect('vuelos')

#BUSCAR VUELO
def buscar_vuelo(request):
    vuelo = None
    formulario = VueloBuscarForm()
    
    if request.method == 'POST':
        formulario = VueloBuscarForm(request.POST)
        if formulario.is_valid():
            codigo = formulario.cleaned_data['codigo']
            vuelo = VueloService.buscar_vuelo_por_codigo(codigo)
            if vuelo is None:
                messages.error(request,"Sin resultados")

    return render(request, 'buscar-vuelo.html', {
        'form': formulario,
        'vuelo': vuelo
    })

#VER TODOS LOS VUELOS
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR']).exists())
def listar_vuelos(request):
    vuelos = EmpleadoService.ver_vuelos()
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

#MOSTRAR RESERVAS HECHAS
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR']).exists())
def mostrar_reservas(request, vuelo_id):
    reservas = Reserva.objects.filter(vuelo__id=vuelo_id)
    if not reservas:
        messages.error(request,"No hay reservas asociadas a este vuelo aún")
    return render(request,"reservas.html",{'reservas':reservas})


#SOBRE EMPLEADOS (EL ADMINISTRADOR MANIPULA LA INFORMACIÓN)
#VER EMPLEADOS
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['ADMINISTRADOR']).exists())
def ver_empleados(request):
    empleados = AdministradorService.ver_empleados()
    return render(request,'empleados.html',{'empleados':empleados})

#CREAR EMPLEADO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['ADMINISTRADOR']).exists())
def crear_empleado(request):
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            AdministradorService.agregar_empleado(
                formulario.cleaned_data['nombre'],
                formulario.cleaned_data['apellido'],
                formulario.cleaned_data['email'],
                formulario.cleaned_data['telefono'],
                formulario.cleaned_data['salario'],
                date.today()
            )
            #messages.success(request,"Empleado cargado exitosamente")
            return redirect('inicio')
    else:
        formulario = EmpleadoForm()
    return render(request,'crear-empleado.html',{'form':formulario})

#BUSCAR EMPLEADO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['ADMINISTRADOR']).exists())
def buscar_empleado(request):
    empleado = None
    formulario = EmpleadoBuscarForm()
    if request.method == 'POST':
        formulario = EmpleadoBuscarForm(request.POST)
        if formulario.is_valid():
            id = formulario.cleaned_data['id']
            empleado = AdministradorService.buscar_empleado(id)
            if empleado is None:
                messages.error(request,"Sin resultados")

    return render(request, 'buscar-empleado.html', {
        'form': formulario,
        'empleado': empleado
    })

#MODIFICAR EMPLEADO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['ADMINISTRADOR']).exists())
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        formulario = EmpleadoEditarForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados')  
    else:
        formulario = EmpleadoEditarForm(instance=empleado)

    return render(request, 'editar-empleado.html', {'form': formulario})

#ELIMINAR EMPLEADO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['ADMINISTRADOR']).exists())
def eliminar_empleado(request, empleado_id):
    empleado = AdministradorService.eliminar_empleado(empleado_id)
    if empleado:
        messages.success(request,"Empleado eliminado correctamente")
    else:
        raise Http404("Empleado a eliminar no encontrado")
    return redirect('empleados')
    


#SOBRE LOGIN, REGISTRO Y LOGOUT
#HACER EL LOGIN Y VERIFICAR SI EL QUE INGRESA ES UN PASAJERO, UN EMPLEADO O UN ADMIN, O NADA
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            grupos = user.groups.values_list('name', flat=True)

            if 'administrador' in grupos:
                return redirect('inicio')  # vista para admins
            elif 'pasajero' in grupos:
                return redirect('inicioPasajero')  # vista para pasajeros
            elif 'empleado' in grupos:
                return redirect('inicioEmpleado') #vista para empleados
            else:
                messages.error(request, 'No tenés permisos asignados.')
                return redirect('login')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')




#SOBRE PASAJEROS
#MOSTRAR VUELOS PARA EL PASAJERO
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['PASAJERO']).exists())
def listar_vuelos_pasajero(request):
    vuelos = EmpleadoService.ver_vuelos()
    return render(request,'index-pasajero.html',{'vuelos':vuelos})

#CREAR RESERVA
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['PASAJERO']).exists())
def crear_reserva(request, vuelo_id, pasajero_id):
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            try:
                pasajero = get_object_or_404(Usuario, user__id=pasajero_id)
                vuelo = get_object_or_404(Vuelo, id=vuelo_id)
                PasajeroService.crear_reserva(
                    #formulario.cleaned_data['codigo'],
                    pasajero,
                    vuelo,
                    formulario.cleaned_data['cantidad'],
                    vuelo.fecha
                )
                messages.success(request, "Reserva creada exitosamente")
                return redirect('inicioPasajero')
            except Exception as e:
                messages.error(request, f"Hubo un error al generar la reserva {e}")
        else:
            messages.error(request, "Formulario inválido")
    else:
        formulario = ReservaForm()

    return render(request, 'crear-reserva.html', {'form': formulario})

#VERIFICAR SI UN PASAJERO HIZO RESERVA EN UN VUELO PARA SABER QUE BOTÓN MUESTRO
#Esto es una configuración adicional, para mejorar la experiencia de usuario
#Lo hice más que nada por regla de negocio básica: no se pueden hacer más de una reserva sobre un mismo vuelo
def tiene_reserva(request, id_pasajero, id_vuelo):
    reserva_encontrada = Reserva.objects.filter(pasajero__user__id=id_pasajero, vuelo=id_vuelo).exists()
    return reserva_encontrada

#Una nueva función para listar los vuelos pero viendo si tienen reserva o no, esta ligada a la función tiene_reserva !!
#Es la función que actualmente uso para listar las reservas, no la otra
@login_required
def listar_vuelos_pasajero_con_filtro(request):
    vuelos = EmpleadoService.ver_vuelos()
    usuario = request.user
    vuelos_info = []
    for vuelo in vuelos:
        ya_reservado = tiene_reserva(request, usuario.id, vuelo.id)
        vuelos_info.append({
            'vuelo': vuelo,
            'ya_reservado': ya_reservado
        })

    return render(request, 'index-pasajero.html', {'vuelos_info': vuelos_info})

#VER RESERVAS: Individuales para cada pasajero 
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['PASAJERO']).exists())
def listar_reservas_pasajero(request, id_pasajero):
    reservas = Reserva.objects.filter(pasajero__user__id=id_pasajero)
    if not reservas.exists():
        messages.warning(request, "No tenés reservas hechas aún")

    return render(request, 'listar_reservas.html', {'reservas': reservas})

#CANCELAR RESERVA
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['PASAJERO']).exists())
def eliminar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, id=id_reserva)
    reserva.delete()
    messages.success(request, "Reserva eliminada correctamente.")
    return redirect('reservas', id_pasajero=reserva.pasajero.user.id)





#LOGIN DE USUARIOS
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('inicio')
        else:
            messages.warning(request,"No se ha podido identificar en el sistema")
    return render(request,'login.html')

#REGISTRO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save() 
            messages.success(request, "Usuario registrado correctamente. Inicie sesión.")
            return redirect('login')  # Redirigir a login luego de registrar
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

#LOGOUT
def logout(request):
    auth_logout(request)
    return redirect('login')


#CONFIGURAR PERFIL (ESTO LO PUEDEN HACER TODOS)
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['EMPLEADO', 'ADMINISTRADOR','PASAJERO']).exists())
#Hay que considerar varios escenarios para esta función porque necesito usar tanto el modelo Usuario como el modelo User de Django
def configurar_perfil(request, usuario_id):
    usuario = get_object_or_404(Usuario, user_id=usuario_id)

    user = usuario.user
    #No permitir que cualquier usuario pueda modificar cualquier perfil, porque los id se pasan por url
    #Se que es medio peligroso hacer eso, por eso lo validé acá 
    if(request.user.id != usuario_id):
        return redirect('inicio')
    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)

        if form.is_valid():
            #Guardar datos del modelo Usuario
            form.save()

            #Guardar datos del modelo User
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.save()

            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('inicio')

    else:
        #Precargar los campos del modelo User
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
        }
        form = UsuarioEditarForm(instance=usuario, initial=initial_data)

    return render(request, 'configurar-perfil.html', {'form': form})
    