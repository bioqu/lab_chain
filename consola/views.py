from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return render(request, "consola/indice.html")

def usuarios_lab(request):
    return render(request, "consola/usuarios_lab.html")
 
def reactivos(request):
    return render(request, "consola/reactivos.html") 

def ingresar_reactivos(request):
    return render(request, "consola/ingresar_reactivos.html") 

def editar_reactivos(request):
    return render(request, "consola/editar_reactivos.html")  

def experimentos(request):
    return render(request, "consola/experimentos.html")  