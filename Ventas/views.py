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

def DetalleCita(request):
    return render(request, "DetalleCita.html")

def AdminVentas(request):
    return render(request, "Ventas.html")

def AgregarServicio(request):
    return render(request, "AgregarServicio.html")

def ListarServicio(request):
    return render(request, "ListarServicios.html")
    
def EditarServicio(request):
    return render(request, "EditarServicio.html")

def AgregarCita(request):
    return render(request, "AgregarCita.html")

def ListarCita(request):
    return render(request, "ListarCitas.html")
    
def EditarCita(request):
    return render(request, "EditarCita.html")