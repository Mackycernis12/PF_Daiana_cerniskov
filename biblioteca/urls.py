"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("principal" ,views.inicio, name="principal"),
    path("alta_clientes", views.registrar_clientes, name="alta_clientes"),
    path("alta_libros", views.alta_libros, name="alta_libros"),
    path("buscar_libros",views.buscar_libros, name="buscar_libros"),
    path("buscar", views.buscar),
    path("ver_libros", views. ver_libros, name="ver_libros"),
    path("eliminar_libros/<int:id>", views.eliminar_libros, name="eliminar_libros"),
    path("editar_libros/<int:id>", views.editar_libros, name="editar_libros"),
    path("editar_libros", views.editar_libros, name="editar_libros"),
    path("ver_clientes", views. ver_clientes, name="ver_clientes"),
    path("eliminar_cliente/<int:id>", views.eliminar_cliente, name="eliminar_cliente"),
    path("editar_cliente/<int:id>", views.editar_cliente, name="editar_cliente"),
    path("editar_cliente", views.editar_cliente, name="editar_cliente"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("editar_perfil", views.editar_perfil, name="Editar_perfil")


]