class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session["carrito"]
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito=carrito

    def guardarCarrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True       
    
    def agregarServicio(self,servicio):
        id_s=str(servicio.id_servicio)
        if id_s not in self.carrito.keys():
            self.carrito[id_s]={
                "id_servicio":servicio.id_servicio,
                "nombre":servicio.nombre,
                "acumulado":servicio.precio
            }
        self.guardarCarrito()
    

    def eliminarCarrito(self,servicio):
        id_s=str(servicio.id_servicio)
        if id_s in self.carrito:
            del self.carrito[id_s]
            self.guardarCarrito()

    def limpiarCarrito(self):
        self.session["carrito"]={}
        self.session.modified=True

