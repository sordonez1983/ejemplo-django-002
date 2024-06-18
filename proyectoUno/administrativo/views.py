from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from administrativo.models import *

# Create your views here.

def listar_estudiantes(request):
    """
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # equipos
    estudiantes = Estudiante.objects.all()
    # se obtiene el número de elementos de la lista
    numero_estudiantes = len(estudiantes)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': numero_estudiantes}
    return render(request, 'listar_estudiantes.html', informacion_template)


def listar_telefonos(request):
    """
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # equipos
    telefonos = NumeroTelefonico.objects.all()
    # se obtiene el número de elementos de la lista
    numero_telefonos = len(telefonos)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'telefonos': telefonos, 'numero_telefonos': numero_telefonos}
    return render(request, 'listar_telefonos.html', informacion_template)
