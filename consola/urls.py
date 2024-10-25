from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name = "consola-indice"),
    path("miembros/", views.usuarios_lab, name = "consola-usuarios_lab"),
    path("reactivos/", views.reactivos, name = "consola-reactivos"),
    path("reactivos/ingresar/", views.ingresar_reactivos, name = "consola-ingresar_reactivos"),
    path("reactivos/editar/", views.editar_reactivos, name = "consola-editar_reactivos"),    
    path("experimentos/", views.experimentos, name = "consola-experimentos"),
]