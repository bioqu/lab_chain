from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name = "consola-indice"),
    path("miembros/", views.usuarios_lab, name = "consola-usuarios_lab"),
    
]