
from django.contrib import admin
from django.urls import path
from app_sistema import views
from django.contrib.auth import views as auth_views
from app_sistema.forms import CustomLoginForm,RegistroForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('inicio/',views.index, name='inicio'),
    path('nuevoVuelo/',views.crear_vuelo, name='nuevo_vuelo'),
    path('vuelos/',views.listar_vuelos,name='vuelos'),
    path('login/', views.login_view, name='login'), 
    path('logout/',views.logout,name='logout'),
    path('registro/',views.registro,name='registro'),
    path('pasajeroInicio/',views.listar_vuelos_pasajero_con_filtro,name='inicioPasajero'),
    path('editarVuelo/<int:vuelo_id>/',views.editar_vuelo,name='editarVuelo'),
    path('eliminarVuelo/<int:vuelo_id>/',views.eliminar_vuelo,name='eliminarVuelo'),
    path('buscarVuelo/',views.buscar_vuelo,name='buscarVuelo'),
    path('crearReserva/<int:vuelo_id>/<int:pasajero_id>/',views.crear_reserva,name='crearReserva'),
    path('reservas/<int:id_pasajero>/', views.listar_reservas_pasajero, name='reservas'),
    path('cancelarReserva/<int:id_reserva>/', views.eliminar_reserva, name='cancelarReserva'),
    path('inicioEmpleado/',views.index, name='inicioEmpleado'),
    path('empleados/',views.ver_empleados,name='empleados'),
    path('cargarEmpleado/',views.crear_empleado,name='crearEmpleado'),
    path('buscarEmpleado/',views.buscar_empleado,name='buscarEmpleado'),
    path('editarEmpleado/<int:empleado_id>',views.editar_empleado,name='editarEmpleado'),
    path('eliminarEmpleado/<int:empleado_id>/',views.eliminar_empleado,name='eliminarEmpleado'),
    path('reservasVuelo/<int:vuelo_id>/',views.mostrar_reservas, name='reservasVuelo'),
    path('configurarPerfil/<int:usuario_id>/',views.configurar_perfil,name='configurarPerfil')
]
