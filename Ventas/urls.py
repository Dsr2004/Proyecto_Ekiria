from django.urls import path
from Ventas.views import Catalogo, TerminarPedido, Calendario, ServiciosPersonalizados,DetalleCita, AdminVentas,AgregarServicio,ListarServicio, EditarServicio, AgregarCita,ListarCita, EditarCita

urlpatterns = [
    path('Catalogo/', Catalogo, name="catalogo"),
    path('TerminarPedido/', TerminarPedido, name="TerminarPedido"),
    path('Calendario/', Calendario, name="calendario"),
    path('PersonalizarSer/', ServiciosPersonalizados, name="personalizar"),
    path('DetalleCita/', DetalleCita, name="detalleCita"),
    path('AdminVentas/', AdminVentas, name="adminVentas"),
    path('AgregarServicio/', AgregarServicio, name="agregarServicio"),
    path('ListadoServicios/', ListarServicio, name="listarServicios"),
    path('EditarServicio/', EditarServicio, name="editarServicio"),
    path('AgregarCita/', AgregarCita, name="agregarCita"),
    path('ListadoCitas/', ListarCita, name="listarCitas"),
    path('EditarCita/', EditarCita, name="editarCita"),
]

