
from django import forms
from .models import Vuelo, Usuario,Reserva,Empleado
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['codigo','origen','destino','capacidad','fecha','hora_salida','hora_embarque']
        widgets = {
            'codigo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar código'}),
            'origen':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar origen: '}),
            'destino':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar destino: '}),
            'capacidad':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresar capacidad'}),
            'fecha':forms.DateInput(attrs={'class':'form-control','placeholder':'Ingresar fecha del vuelo (FORMATO YYYY-MM-DD): '}),
            'hora_salida':forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingresar hora de salida: '}),
            'hora_embarque':forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingresar hora de embarque: '})
        }
        labels = {
            'codigo':'Código',
            'origen': 'Origen',
            'destino':'Destino',
            'capacidad':'Capacidad',
            'fecha':'Fecha',
            'hora_salida':'Hora de salida',
            'hora_embarque':'Hora de embarque'
        }

class VueloBuscarForm(forms.Form):
   codigo = forms.CharField(
        label='Código',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar código'
        })
   )


class VueloEditarForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['codigo','origen','destino','capacidad','fecha','hora_salida','hora_embarque']
        widgets = {
            'codigo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo código'}),
            'origen':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo origen: '}),
            'destino':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo destino: '}),
            'capacidad':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresar nueva capacidad'}),
            'fecha':forms.DateInput(attrs={'class':'form-control','placeholder':'Ingresar nueva fecha del vuelo (FORMATO YYYY-MM-DD): '}),
            'hora_salida':forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingresar nueva hora de salida: '}),
            'hora_embarque':forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingresar nueva hora de embarque: '})
        }
        labels = {
            'codigo':'Código',
            'origen': 'Origen',
            'destino':'Destino',
            'capacidad':'Capacidad',
            'fecha':'Fecha',
            'hora_salida':'Hora de salida',
            'hora_embarque':'Hora de embarque'
        }

class EmpleadoEditarForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','email','telefono','salario']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo nombre: '}),
            'apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo apellido: '}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo email: '}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo telefono: '}),
            'salario':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo salario: '})
        }
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'telefono':'Telefono',
            'salario':'Salario'
        }

class UsuarioEditarForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo nombre: '}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo apellido: '}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo email: '}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo username: '}))

    class Meta:
        model = Usuario
        fields = ['telefono']

        widgets = {
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nuevo telefono: '})
        }
        labels = {
            'telefono': 'Teléfono'
        }


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cantidad']
        widgets = {
            'cantidad':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresar cantidad'})
        }
        labels = {
            'cantidad':'Cantidad'
        }

#FORMULARIO PARA CARGAR EMPLEADO
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = ['fecha_ingreso']
        fields = ['nombre','apellido','email','telefono','salario']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nombre: '}),
            'apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nombre: '}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nombre: '}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar nombre: '}),
            'salario':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresar salario: '})
        }
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'telefono':'Telefono',
            'salario':'Salario'
        }

#FORMULARIO PARA BUSCAR UN EMPLEADO A PARTIR DE SU ID
class EmpleadoBuscarForm(forms.Form):
   id = forms.CharField(
        label='ID:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresar ID del empleado a buscar: '
        })
   )

#FORMULARIO DE INICIO DE SESIÓN (ALTERNATIVO)
class CustomLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Ingresar nombre de usuario: '})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Ingresar contraseña: '})


class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=100)  # campos extra
    pasaporte = forms.CharField(max_length=100) 
    class Meta:
        model = User  
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # Crear el perfil Usuario vinculado
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        telefono = self.cleaned_data['telefono']
        pasaporte = self.cleaned_data['pasaporte']
        if commit:
            user.save()
            #Aparte de crearlo, necesito guardarlo en la BBDD
            Usuario.objects.create(user=user, telefono=telefono,pasaporte=pasaporte, estado=1)
            #Le asigno el rol de pasajero, sacado de "grupos" que hice en el panel de admin
            #el rol por defecto es: pasajero, pero yo le pongo ahora empleado, para creame un perfil
            grupo_pasajero = Group.objects.get(name='pasajero')
            user.groups.add(grupo_pasajero)
        return user
