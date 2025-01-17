class Carro:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        self.carro = carro
    def items(self):
        return self.carro.items()  # Devuelve los elementos del carrito
    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            # Verifica si la imagen no es nula antes de acceder a su URL
            imagen_url = producto.imagen.url if producto.imagen else None
            
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": imagen_url  # Asigna la URL de la imagen o None
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break

        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True
    def eliminar(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    def restar_producto(self, producto):
        for key,value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"]= value["cantidad"]-1
                value["precio"] = float(value["precio"]) - producto.precio

                if value["cantidad"] <1:
                    self.eliminar(producto)
                    break
        self.guardar_carro()
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified= True