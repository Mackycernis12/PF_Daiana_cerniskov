from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Users_form(forms.Form):
    usuario = forms.CharField(max_length=60)
    clave = forms.IntegerField()


class clientes_form(forms.Form):
    nombre = forms.CharField(max_length=60)
    email = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)

class libros_form(forms.Form):
    nombre = forms.CharField(max_length=150)
    Editorial = forms.CharField(max_length=100)
    año_publicacion = forms.IntegerField()

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Buscar por nombre', max_length=100)

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar e-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k:"" for k in fields}


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'avatar']