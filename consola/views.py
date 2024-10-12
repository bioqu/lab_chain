from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return HttpResponse("Pagina de Indice")

def usuarios_lab(request):
    return HttpResponse("Pagina de miembros de laboratorio")
