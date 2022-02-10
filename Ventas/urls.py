from django.urls import path 
from Ventas.views import Catalogo, TerminarPedido, Calendario, ServiciosPersonalizados,DetalleCita, AdminVentas,AgregarServicio,ListarServicio, EditarServicio, AgregarCita,ListarCita, EditarCita, Carrito,ServicioDetalle, pruebas
app_name="Ventas"
urlpatterns = [
    path('Catalogo/', Catalogo.as_view(), name="catalogo"),
    path('Carrito/', Carrito.as_view(), name="carrito"),
    path('TerminarPedido/', TerminarPedido.as_view(), name="TerminarPedido"),
    path('Calendario/', Calendario.as_view(), name="calendario"),
    path('PersonalizarSer/', ServiciosPersonalizados.as_view(), name="personalizar"),
    path('DetalleCita/', DetalleCita.as_view(), name="detalleCita"),
    path('AdminVentas/', AdminVentas.as_view(), name="adminVentas"),
    path('AgregarServicio/', AgregarServicio.as_view(), name="agregarServicio"),
    path('ListadoServicios/', ListarServicio.as_view(), name="listarServicios"),
    path('EditarServicio/<int:pk>', EditarServicio.as_view(), name="editarServicio"),
    path('AgregarCita/', AgregarCita.as_view(), name="agregarCita"),
    path('ListadoCitas/', ListarCita.as_view(), name="listarCitas"),
    path('EditarCita/', EditarCita.as_view(), name="editarCita"),
    path('pruebas/', pruebas, name="pruebas"), 
    path('<slug>/', ServicioDetalle.as_view(), name="detalleSer"),                      
]

