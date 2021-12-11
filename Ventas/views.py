from django.shortcuts import render
from django.http import HttpResponse

def Catalogo(request):
    return render(request, "Catalogo.html")

def TerminarPedido(request):
    return render(request, "TerminarPedido.html")

def Calendario(request):
    return render(request, "Calendario.html")

def ServiciosPersonalizados(request):
    return render(request, "AddservicioPer.html")


