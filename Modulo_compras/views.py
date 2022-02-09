from django.shortcuts import render, redirect
from Modulo_compras.forms import ProveedorForm
from .models import Proveedor

def Productos (request):
    return render(request,"Productos.html")

def Conf_compra (request):
    return render(request,"conf_compra.html")

def Listarprov(request):
    Proveedores=Proveedor.objects.all()
    prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form , 'proveedores': Proveedores})


def Crearprov(request):

    if request.method == 'POST':
        prov_form = ProveedorForm(request.POST)
        if prov_form.is_valid():
            prov_form.save()
            return redirect('listarprov')

    else:

        prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form})
