from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Editorial: {self.Editorial}, Año de publicación: {self.año_publicacion}"


class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, E-mail: {self.email}, Dirección: {self.direccion}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) 
