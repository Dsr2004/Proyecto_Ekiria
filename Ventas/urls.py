from django.urls import path 
from Ventas.views import *
from Ventas import carrito
app_name="Ventas"
urlpatterns = [
    path('AddtoCarrito/', carrito.actualizarItem, name="addtoCarrito"),

    path('AgregarCita/', AgregarCita.as_view(), name="agregarCita"),
    path('ListadoCitas/', ListarCita.as_view(), name="listarCitas"),
    path('DetalleCita/', DetalleCita.as_view(), name="detalleCita"),
    path('EditarCita/', EditarCita.as_view(), name="editarCita"),

    path('Catalogo/', Catalogo.as_view(), name="catalogo"),
    path('AgregarServicioCatalogo/', AgregarServicioalCatalogo.as_view(), name="agregarServicioCatalogo"),
    path("CambiarEstadoServicioEnCatalogo/",CambiarEstadoServicioEnCatalogo, name="cambiarEstadoServicioEnCatalogo"),
    
    path('pruebas/', pruebas, name="pruebas"), 

    path('Carrito/', Carrito, name="carrito"),
    path('TerminarPedido/', TerminarPedido, name="terminarPedido"),
    path('Calendario/', Calendario.as_view(), name="calendario"),
    path('PersonalizarSer/', ServiciosPersonalizados.as_view(), name="personalizar"),
    
    
    path('AdminVentas/', AdminVentas.as_view(), name="adminVentas"),
    path('AgregarTipoServicio/', AgregarTipo_Servicio.as_view(), name="agregarTipoServicio"),
    path('EditarTipoServicio/<int:pk>', EditarTipo_Servicio.as_view(), name="editarTipoServicio"),
    path('EditarEstadoTipoServicio/', CambiarEstadoTipoServicio, name="editarEstadoTipoServicio"),
    path('ElimiarTipoServicio/<int:pk>', ElimininarTipoServicio.as_view(), name="eliminarTipoServicio"),

    path('AgregarServicio/', AgregarServicio.as_view(), name="agregarServicio"),
    path('ListadoServicios/', ListarServicio.as_view(), name="listarServicios"),
    path('CambiarEstadoServicio/', CambiarEstadoServicio, name="cambiarEstadoServicio"),
    path('EditarServicio/<int:pk>', EditarServicio.as_view(), name="editarServicio"),
    path('<slug>/', ServicioDetalle.as_view(), name="detalleSer"), 
    

 

    
                         
]

