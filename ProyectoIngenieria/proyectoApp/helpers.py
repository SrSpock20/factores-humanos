
class AreaEstructura:


    def __init__(self,nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return self.nombre +":"+ str(self.cantidad)


class Empleado_Max:

    def __init__(self,nombre, area,cantidad):
        self.nombre = nombre
        self.area = area
        self.cantidad = cantidad

    def __str__(self):
        return self.nombre + ":" + str(self.cantidad) +" "+self.area
