from django.http import HttpResponse
from django.template import loader

# Create your views here.

def productos(request):
    datos = {"Libro":"Dune", "Año":1965}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               