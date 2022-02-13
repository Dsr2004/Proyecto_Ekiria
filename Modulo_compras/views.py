from django.shortcuts import render, redirect
from Modulo_compras.forms import ProveedorForm
from .models import Proveedor
from django.http import HttpResponse



def Productos (request):
    return render(request,"Productos.html")

def Conf_compra (request):
    return render(request,"conf_compra.html")

def Listarprov(request):
    Proveedores=Proveedor.objects.all()
    prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form , 'proveedores': Proveedores})
    # return redirect('proveedor')


def Crearprov(request):

    if request.method == 'POST':
        prov_form = ProveedorForm(request.POST)
        if prov_form.is_valid():
            prov_form.save()
            return redirect('listarprov')

    else:

        prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form})

def Eliminarprov(request, id_proveedor):
    prov_form =Proveedor.objects.get(id_proveedor=id_proveedor)
    prov_form.delete()
    return redirect('listarprov')
    # return render(request,'proveedores.html',{'prov_form':prov_form})
   
