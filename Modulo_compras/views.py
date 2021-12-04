from django.shortcuts import render

def Proveedor (request):
    return render(request,"proveedores.html")

def Productos (request):
    return render(request,"Productos.html")

