import math
class Patron():
    def __init__(self):
        self.caracteristicas=[]
        self.clase = None
        self.distancia = None
        self.orden = None

    def addCaracteristica(self, caracteristica):
        self.caracteristicas.append(caracteristica)

    def setCaracteristicas(self, caracteristicas):
        self.caracteristicas = caracteristicas

    def setClase(self, clase):
        self.clase = clase

    def getClase(self):
        return self.clase

    def setOrden(self, orden):
        self.orden = orden
    
    def getOrden(self):
        return self.orden

    def getCaracteristicaIndex(self, index):
        return self.caracteristicas[index]

    def getCaracteristicas(self):
        return self.caracteristicas

    def calcualarDistancia(self, patronDesconocido):
        distancia = 0
        
        for index in range(len(self.caracteristicas)):
            distancia += (patronDesconocido.getCaracteristicaIndex(index) - self.caracteristicas[index]) ** 2

        distancia = math.sqrt(distancia)
        self.distancia = distancia

        return distancia

    def getDistancia(self):
        return self.distancia