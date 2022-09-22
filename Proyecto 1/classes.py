import this


class Vehiculo:
    def __init__(self, num_id, nom, stock, pais, tipo, modelo):
        self.numero_identificacion = num_id
        self.nombre = nom
        self.cant_stock = stock
        self.pais_origen = pais
        self.tipo = tipo
        self.modelo = modelo

    def get_numero_identificacion(self):
        return self.numero_identificacion
    
    def set_numero_identificacion(self, new):
        self.numero_identificacion = new

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, new):
        self.nombre = new

    def get_pais_origen(self):
        return self.pais_origen

    def set_pais_origen(self, new):
        self.pais_origen = new

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, new):
        self.tipo = new

    def get_modelo(self):
        return self.tipo

    def set_modelo(self, new):
        self.tipo = new

    def calcular_impuestos(self, año_vigente):
        n = año_vigente - self.modelo
        match n:
            case 1|0:
                return 20000
            
            case 2|3:
                return 10000
            
            case 4|5:
                return 5000

            case _:
                return 0

    def to_string(self):
        cadena = '>>>Vehiculo numero: {:<10}'.format(self.numero_identificacion)
        cadena += '>>>Nombre: {:<20}'.format(self.nombre)
        cadena += '>>>Cantidad de stock: {:<10}'.format(self.cant_stock)
        cadena += '>>>Pais de origen: {:<10}'.format(self.pais_origen)
        cadena += '>>>Tipo de vehiculo: {:<10}'.format(self.tipo)
        cadena += '>>>Modelo año: {:<10}'.format(self.modelo)
        print(cadena)
        return

    
    