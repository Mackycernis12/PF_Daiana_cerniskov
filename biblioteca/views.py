from django.shortcuts import render, redirect
from biblioteca.models import Libros,Clientes, UserProfile
from django.http import HttpResponse
from biblioteca.forms import clientes_form, libros_form, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login

from .forms import CustomUserCreationForm
from PIL import Image, ExifTags

# Create your views here.

def inicio(request):
    return render(request, "principal.html")

@login_required
def registrar_clientes(request):
    if request.method == "POST":
        mi_formulario_cliente = clientes_form(request.POST)
        if mi_formulario_cliente.is_valid():
            datos_cliente = mi_formulario_cliente.cleaned_data
            cliente = Clientes(nombre=datos_cliente['nombre'], email=datos_cliente['email'], direccion=datos_cliente['direccion'])
            cliente.save()

            messages.success(request, 'El cliente se registró exitosamente. Para modificaciones/bajas vaya a la sección lista de clientes o si desea registrar otro cliente inserte la información deseada')

            return render(request, "form_registro_clientes.html")
    
    return render(request, "form_registro_clientes.html")
    

 

@login_required
def alta_libros(request):
    if request.method == "POST":
        mi_formulario_libros = libros_form(request.POST)
        if mi_formulario_libros.is_valid():
            datos_libros = mi_formulario_libros.cleaned_data
            libros = Libros(nombre=datos_libros['nombre'], Editorial=datos_libros['Editorial'], año_publicacion=datos_libros['año_publicacion'])
            libros.save()

            messages.success(request, 'El libro se registró exitosamente. Para modificaciones/bajas vaya a la sección libros disponibles o si desea registrar otro libro inserte la información deseada')
            return render(request, "form_registro_libros.html")

    return render(request, "form_registro_libros.html")


@login_required
def buscar_libros(request):
    return render(request, "buscar_libros.html")

@login_required
def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        librerias = Libros.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"librerias":librerias})
    else:
        return HttpResponse("campo vacio")

@login_required
def ver_libros(request):
    libros_ver = Libros.objects.all()
    return render(request, "libros.html", {"libros_ver":libros_ver})

@login_required
def eliminar_libros(request, id):
    libro = Libros.objects.get(id=id)
    libro.delete()
    return redirect(ver_libros)

@login_required
def editar_libros(request, id):
    libro = Libros.objects.get(id=id)

    if request.method == "POST":
        mi_formulario_edit = libros_form(request.POST)
        if mi_formulario_edit.is_valid():
            datos = mi_formulario_edit.cleaned_data
            libro.nombre = datos['nombre']
            libro.año_publicacion = datos['año_publicacion']
            libro.Editorial = datos['Editorial']
            libro.save()

            return redirect(ver_libros)
    else:
        mi_formulario_edit = libros_form(initial={"nombre": libro.nombre, "año_publicacion": libro.año_publicacion, "Editorial": libro.Editorial})
    return render(request, "editar_libros.html", {"mi_formulario_edit": mi_formulario_edit, "libro": libro}) 

@login_required
def ver_clientes(request):
    clientes_ver = Clientes.objects.all()
    return render(request, "cliente.html", {"clientes_ver":clientes_ver})

@login_required
def eliminar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect(ver_clientes)

@login_required
def editar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = clientes_form(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            cliente.nombre = datos['nombre']
            cliente.email = datos['email']
            cliente.direccion = datos['direccion']
            cliente.save()

            return redirect(ver_clientes)
    else:
        mi_formulario = clientes_form(initial={"nombre": cliente.nombre, "email": cliente.email, "direccion": cliente.direccion})
    return render(request, "editar_cliente.html", {"mi_formulario": mi_formulario, "cliente": cliente}) 



def login_request(Request):
    if Request.method == "POST":
        form = AuthenticationForm(Request, data=Request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            contra = form.cleaned_data["password"]
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(Request, user)               
                user_profile = UserProfile.objects.get(user=user)
                avatar = user_profile.avatar          
                image = Image.open(avatar.path)
                
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            exif = dict(image._getexif().items())
                            if orientation in exif:
                                orientation_value = exif[orientation]
                                break
                    else:
                        orientation_value = 1  
                except (AttributeError, KeyError, IndexError):
                    orientation_value = 1  

                return render(Request, "inicio.html", {"mensaje": f"Bienvenido/a: {usuario}", "avatar": avatar, "orientation": orientation_value})

            else:
                return HttpResponse("Usuario incorrecto")
        else:
            return HttpResponse(f"FORM incorrecto {form}")
    form = AuthenticationForm()
    return render(Request, "login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if request.FILES.get('avatar'):
                user_profile = UserProfile.objects.get_or_create(user=user)[0]
                user_profile.avatar = form.cleaned_data['avatar']
                user_profile.save()
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})



@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        miformulario = UserEditForm(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")


    else:
        miformulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editar_perfil.html", {"miformulario":miformulario, "usuario":usuario} )

