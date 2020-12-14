import math
import numpy as np
class Patron():
    def __init__(self):
        self.caracteristicas=None
        self.clase = None

    def addCaracteristica(self, caracteristica):
        self.caracteristicas.append(caracteristica)

    def setCaracteristicas(self, caracteristicas):
        self.caracteristicas = np.array(caracteristicas)
        # print('Caracteristicas en patron', self.caracteristicas)

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

    def getNumberClass(self):
        number = self.clase.split('c')[1]
        return int(number)