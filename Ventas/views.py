from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


from .forms import ServicioForm, Tipo_servicioForm, EditarTipoServicioForm,CatalogoForm, Servicio_PersonalizadoForm
from .models import Servicio, Tipo_servicio, Servicio_Personalizado, Catalogo
from Ventas import models

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se administra el catalogo
<----------------------------------------------------------------->
"""

class Catalogo(ListView): 
    queryset = Servicio.objects.filter(estado=True)
    context_object_name = "servicios"
    template_name = "Catalogo.html"

class AgregarServicioalCatalogo(View):
    model = Catalogo
    form_class =   CatalogoForm
    template_name = "Catalogo/AgregarServicio.html"
    def get(self, request, *args, **kwargs):
        servicesInCatalogo=models.Catalogo.objects.all()
        servicesInCatalogoList=[]
        if request.is_ajax():
            page = request.GET.get('page')
            try:
                posts = paginator.page(page)
            except Exception as e:
                posts = paginator.page(1)
            except Exception:
                posts = paginator.page(paginator.num_pages)
            services_list = list(posts.object_list.values())
            result = {'has_previous': posts.has_previous(),
                  'has_next': posts.has_next(),
                  'num_pages': posts.paginator.num_pages,
                  'user_li': services_list}
            return JsonResponse(result)
        else:
            for i in servicesInCatalogo:
                id=i.servicio_id.id_servicio
                servicesInCatalogoList.append(id)
            ServiciosNoEnCatalogo=Servicio.objects.exclude(id_servicio__in=servicesInCatalogoList).filter(estado=True)

            paginado=Paginator(ServiciosNoEnCatalogo, 3)
            pagina = request.GET.get("page") or 1
            posts = paginado.get_page(pagina)
            pagina_actual=int(pagina)
            paginas=range(1,posts.paginator.num_pages+1)



        contexto={
            "form":self.form_class,
            "servicios":ServiciosNoEnCatalogo,
            "NoEnCatalogo":posts,
            'paginas':paginas,
            'pagina_actual':pagina_actual
        }

        return render(request, self.template_name, contexto)


class QuitarServicioalCatalogo(DeleteView):
    pass




class Carrito(TemplateView):
    template_name = "Carrito.html"

class TerminarPedido(TemplateView):
    template_name = "TerminarPedido.html"

class Calendario(TemplateView):
    template_name = "Calendario.html"

class ServiciosPersonalizados(CreateView):
    model = Servicio_Personalizado
    form_class = Servicio_PersonalizadoForm
    template_name = "AddservicioPer.html"
    success_url=reverse_lazy("Ventas:catalogo")

    
        
    

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se administra el Admin de las ventas
<----------------------------------------------------------------->
"""

class AdminVentas(TemplateView):
    template_name = "Ventas.html"

    def get(self,request, *args, **kwargs):
        formTipo_Servicio = EditarTipoServicioForm
        servicios=models.Catalogo.objects.all()

        paginado=Paginator(servicios, 5)
        pagina = request.GET.get("page") or 1
        posts = paginado.get_page(pagina)
        pagina_actual=int(pagina)
        paginas=range(1,posts.paginator.num_pages+1)
        #contexto
        context={
            'Tipo_Servicios':Tipo_servicio.objects.all(),
            'form_Tipo_Servicio':formTipo_Servicio,
            'servicios':posts,
            'paginas':paginas,
            'pagina_actual':pagina_actual
        }
        
        return render(request, self.template_name, context)
    

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se administran los tipos de servicios
<----------------------------------------------------------------->
"""
class AgregarTipo_Servicio(CreateView):#crear
    model = Tipo_servicio
    form_class = Tipo_servicioForm
    template_name = "Tipo_Servicio/Tipo_servicioAdd.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_TipoServicio = Tipo_servicio(
                    nombre = form.cleaned_data.get('nombre'),
                    estado = form.cleaned_data.get('estado')
                )
                nuevo_TipoServicio.save()
                mensaje = f"{self.model.__name__} registrado correctamente"
                error = "No hay error!"
                response = JsonResponse({"mensaje":mensaje, "error":error})
                response.status_code = 201
                return response
            else:
                errores=form.errors
                mensaje = f"{self.model.__name__} no se ha podido actualizar!"
                response = JsonResponse({"mensaje":mensaje, 'errors': errores})
                response.status_code = 400
                return response
        else:
            return redirect("Ventas:adminVentas")
            

class EditarTipo_Servicio(UpdateView):#actualziar
    model = Tipo_servicio
    form_class = Tipo_servicioForm
    template_name = "Tipo_Servicio/Tipo_servicio.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f"{self.model.__name__} actualizado correctamente"
                error = "No hay error!"
                response = JsonResponse({"mensaje":mensaje, "error":error})
                response.status_code = 201
                return response
            else:
                errores=form.errors
                mensaje = f"{self.model.__name__} no se ha podido actualizar!"
                response = JsonResponse({"mensaje":mensaje, 'errors': errores})
                response.status_code = 400
                return response
        else:
            return redirect("Ventas:adminVentas")

class ElimininarTipoServicio(DeleteView):
    model = Tipo_servicio
    template_name = "Tipo_Servicio/EliminarTipoServicio.html"
    success_url = reverse_lazy("Ventas:adminVentas")


def CambiarEstadoTipoServicio(request):
    if request.method=="POST":
        id = request.POST["estado"]
        update=Tipo_servicio.objects.get(id_tipo_servicio=id)
        estatus=update.estado
        if estatus==True:
            update.estado=False
            update.save()
        elif estatus==False:
            update.estado=True
            update.save()
        else:
            return redirect("Ventas:adminVentas")
        return HttpResponse(update)
    else:
        return redirect("Ventas:adminVentas")

class ElimininarTipoServicio(DeleteView):#eliminar
    model = Tipo_servicio
    template_name = "Tipo_Servicio/EliminarTipoServicio.html"
    success_url = reverse_lazy("Ventas:adminVentas")

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se administran los servicios
<----------------------------------------------------------------->
"""

class AgregarServicio(CreateView):#crear
    model = Servicio
    form_class = ServicioForm
    template_name = "AgregarServicio.html"
    success_url = reverse_lazy('Ventas:listarServicios')

    def form_valid(self, form, **kwargs):
        objeto=form.save()
        if objeto.estado == True:
            pk=int(objeto.id_servicio)
            ServicioToCatalogo = models.Catalogo.objects.create(servicio_id=objeto)
            ServicioToCatalogo.save()
        objeto.save()
        return redirect("Ventas:listarServicios")

class EditarServicio(UpdateView):#actualizar
    model = Servicio
    form_class = ServicioForm
    template_name = "EditarServicio.html" 
    success_url = reverse_lazy('Ventas:listarServicios')

class ListarServicio(ListView):#listar
    queryset = Servicio.objects.all()
    context_object_name = "servicios"
    template_name = "ListarServicios.html"

class ServicioDetalle(DetailView):#detalle
    queryset = Servicio.objects.all()
    context_object_name = "DetailSs"
    template_name = "Catalogo/Detalle_Servicio.html"

def CambiarEstadoServicio(request):
    if request.method == "POST":
        id = request.POST["estado"]
        update=Servicio.objects.get(id_servicio=id)
        estatus=update.estado
        if estatus==True:
            update.estado=False
            update.save()
        elif estatus==False:
            update.estado=True
            update.save()
        else:
            return redirect("Ventas:listarServicios")
        return HttpResponse(update)
    else:
        return redirect("Ventas:listarServicios")

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se administran las citas
<----------------------------------------------------------------->
"""

class AgregarCita(TemplateView):
    template_name = "AgregarCita.html"

class ListarCita(TemplateView):
    template_name = "ListarCitas.html"
    
class EditarCita(TemplateView):
    template_name = "EditarCita.html"

class DetalleCita(TemplateView):
   template_name = "DetalleCita.html"

"""
<----------------------------------------------------------------->
Seccion de las Vistas donde se realizan las pruebas
<----------------------------------------------------------------->
"""

def ejemplo(request, id):
    consuta=Servicio.objects.filter(id_servicio=id)

def pruebas(request):
    newsdata = Servicio.objects.all()
    per_page = 4
    obj_paginator = Paginator(newsdata, per_page)
    first_page = obj_paginator.page(1).object_list
    page_range = obj_paginator.page_range

    context = {
    'obj_paginator':obj_paginator,
    'first_page':first_page,
    'page_range':page_range
    }
    #
    if request.method == 'POST':
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values('id', 'title','content'))
        return JsonResponse({"results":results})

    return render(request, 'index.html',context)
    # user_list = Servicio.objects.all().order_by('id_servicio')
    # paginator = Paginator(user_list, 4)
    # if request.method == 'GET':
    # 	users = paginator.page(1)
    # 	return render(request, 'prueba.html', {'users': users})
    # if request.is_ajax():
    #     page = request.GET.get('page')
    #     try:
    #         users = paginator.page(page)
    #     except PageNotAnInteger:
    #         users = paginator.page(1)
    #     except InvalidPage:
    #         users = paginator.page(paginator.num_pages)

    #     user_li = list(users.object_list.values())
    #     # Respectivamente, si hay una página anterior falsa / verdadera, si hay una página siguiente falsa / verdadera, el número total de páginas, los datos de la página actual
    #     result = {'has_previous': users.has_previous(),
    #               'has_next': users.has_next(),
    #               'num_pages': users.paginator.num_pages,
    #               'user_li': user_li}
    #     print(result["user_li"])
    #     return JsonResponse(result)
