class NodoSenal():
    nombre = None
    tiempo = None
    amplitud = None
    siguiente = None


    def __init__(self, nombre, tiempo, amplitud):
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.siguiente = None