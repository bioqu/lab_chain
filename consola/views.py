from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return render(request, "consola/indice.html")

def usuarios_lab(request):
    return render(request, "consola/usuarios_lab.html")
  