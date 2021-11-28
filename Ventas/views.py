from django.shortcuts import render
from django.http import HttpResponse

def Catalogo(request):
    return render(request, "Catalogo.html")

def Carrito(request):
    return render(request, "Carrito.html")

def Calendario(request):
    return render(request, "Calendario.html")

def ServiciosPersonalizados(request):
    return render(request, "AddservicioPer.html")


