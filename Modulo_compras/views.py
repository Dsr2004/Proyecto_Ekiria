import json
from django.shortcuts import render, redirect
from Modulo_compras.forms import ProveedorForm
from .models import Proveedor
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



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

         
        messages.error(request, "Error")
    return render(request, 'page.html', {'form':form_class()})

def Eliminarprov(request, id_proveedor):
    prov_form =Proveedor.objects.get(id_proveedor=id_proveedor)
    prov_form.delete()
    return redirect('listarprov')
    # return render(request,'proveedores.html',{'prov_form':prov_form})


def Modificarprov(request):
    id_proveedor= request.POST.get("id_proveedor")
    form=Proveedor.objects.filter(id_proveedor=id_proveedor).first()
    Proveedores=ProveedorForm(instance=form)
    return render(request,'modificarprov.html',{'proveedores': Proveedores , 'Form':form, 'id':id_proveedor})

def Actprov (request):
    pk = request.POST.get("id_proveedor")
    prov_form=Proveedor.objects.get(id_proveedor=pk)
    Proveedores=ProveedorForm(request.POST, instance=prov_form)
    if Proveedores.is_valid():
       Proveedores.save()
    return redirect('listarprov')
   
