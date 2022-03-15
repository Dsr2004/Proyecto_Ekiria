import json
from django.http import JsonResponse

from Usuarios.models import Usuario
from .models import *


def actualizarItem(request):
    data = request.POST
    servicioid = data["servicioId"]
    accion = data["accion"]
    

    cliente = Usuario.objects.get(id_usuario=3)
    servicio= Servicio.objects.get(id_servicio=servicioid)
    pedido,creado = Pedido.objects.get_or_create(cliente_id=cliente, completado=False)

    itemPedio, creado = PedidoItem.objects.get_or_create(pedido_id=pedido,servicio_id=servicio)

    if accion== "remove":
        itemPedio.delete()
    
    return JsonResponse('Item fue anadido', safe=False)