from gc import get_objects
import json
from pickle import TRUE
from django.shortcuts import render, redirect
from Modulo_compras.forms import ProveedorForm
from .models import Proveedor
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView



def Productos (request):
    return render(request,"Productos.html")

def Conf_compra (request):
    return render(request,"conf_compra.html")

def Listcompra(request):
    Proveedores=Proveedor.objects.all()
    prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form , 'proveedores': Proveedores})

def Listarprov(request):
    Proveedores=Proveedor.objects.all()
    prov_form=ProveedorForm()
    return render(request,'proveedores.html',{'prov_form':prov_form , 'proveedores': Proveedores})
    # return redirect('proveedor')


# def Crearprov(request):

#     if request.method == 'POST':
#         prov_form = ProveedorForm(request.POST)
#         if prov_form.is_valid():
#             prov_form.save()
#             return redirect('listarprov')


class Crearprov(CreateView):
    model= Proveedor
    form_class=ProveedorForm
    template_name='modalprov/agregarprov.html'

    def post(self,request, *args, **kwargs):  
            prov_form = ProveedorForm(request.POST)
            if prov_form.is_valid():
                prov_form.save()
                return redirect('listarprov')
            else:
                errors=prov_form.errors
                mensaje=f"{self.model.__name__} no ha sido registrado"
                response=JsonResponse({"errors":errors,"mensaje":mensaje})
                response.status_code=400
                return response
   
        
def Eliminarprov(request, id_proveedor):
    prov_form =Proveedor.objects.get(id_proveedor=id_proveedor)
    prov_form.delete()
    return redirect('listarprov')
    # return render(request,'proveedores.html',{'prov_form':prov_form})


class modificarprov(UpdateView):
    model= Proveedor
    form_class=ProveedorForm
    template_name='modalprov/editarprov.html'

    def post(self,request, *args, **kwargs):  
            prov_form = ProveedorForm(request.POST,instance=self.get_object())
            if prov_form.is_valid():
                prov_form.save()
                return redirect('listarprov')
            else:
                errors=prov_form.errors
                mensaje=f"{self.model.__name__} no ha sido registrado"
                response=JsonResponse({"errors":errors,"mensaje":mensaje})
                response.status_code=400
                return response

def Actprov (request):
    pk = request.POST.get("id_proveedor")
    prov_form=Proveedor.objects.get(id_proveedor=pk)
    Proveedores=ProveedorForm(request.POST, instance=prov_form)
    if Proveedores.is_valid():
       Proveedores.save()
    return redirect('listarprov')

def cambiarestado(request):
    if request.is_ajax:
        if request.method=="POST":
            id = request.POST["estado"]
            update=Proveedor.objects.get(id_proveedor=id)
            estatus=update.estado
            if estatus==True:
                update.estado=False
                update.save()
            elif estatus==False:
                update.estado=True
                update.save()
            else:
                return redirect('listarprov')
    return JsonResponse({"kiwi":"yes"})
  



   
