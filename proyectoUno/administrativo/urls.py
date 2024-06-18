"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views


urlpatterns = [
        path('listar/estudiantes', views.listar_estudiantes, name='listar_estudiantes'),
        path('listar/telefonos', views.listar_telefonos, name='listar_telefonos'),
 ]
