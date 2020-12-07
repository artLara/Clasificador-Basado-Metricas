import math
from Patron import *

class clasificadorKNN():
    def __init__(self):
        self.patron = None
        self.patronDesconocido = None
        self.clases = None
        self.representantes = []
        self.patrones = None
        self.k=1

    def getPatronK(self):
        return self.patrones[self.k - 1]

    def setK(self, k):
        self.k = k

    def setPatrones(self, data):
        if self.patronDesconocido is None:
            return

        self.patrones = []
        count = 1
        for key in data:
            print('Clase:', key)
            for index in range(len(data[key][0])):
                patron = Patron()
                patron.setClase(key)
                print('indice=', index)
                for listaPatrones in data[key]:
                    print('Carcateristicas agregada: ', listaPatrones[index])
                    patron.addCaracteristica(listaPatrones[index])

                patron.calcualarDistancia(self.patronDesconocido)
                patron.setOrden(count)
                count += 1
                self.patrones.append(patron)
            
        self.ordenarPatrones()

        for p in self.patrones:
            print('=========')
            print(p.getClase())
            print(p.getCaracteristicas())

    def setPatronDesconcido(self, carcateristicas):
        patron = Patron()
        for carcateristica in carcateristicas:
            patron.addCaracteristica(carcateristica)
        self.patronDesconocido = patron

    def desempateMedia(self):
        distancias={}
        n = {}
        for index in range(self.k):
            if not (self.patrones[index].getClase() in distancias):
                distancias[self.patrones[index].getClase()] = 0
                n[self.patrones[index].getClase()] = 0

            distancias[self.patrones[index].getClase()] += self.patrones[index].getDistancia()
            n[self.patrones[index].getClase()] += 1

        minimo = 0
        claseMinima = ''
        inicial = True
        for key in distancias:
            distancias[key] /= n[key]
            if inicial:
                minimo = distancias[key]
                claseMinima = key
                inicial = False

            if distancias[key] < minimo:
                minimo = distancias[key]
                claseMinima = key

        return claseMinima, distancias
    def desempatePesos(self):
        distancias={}
        n = {}
        for index in range(self.k):
            if not (self.patrones[index].getClase() in distancias):
                distancias[self.patrones[index].getClase()] = 0
                n[self.patrones[index].getClase()] = 0

            distancias[self.patrones[index].getClase()] += 1/self.patrones[index].getDistancia()
            n[self.patrones[index].getClase()] += 1

        minimo = 0
        claseMinima = ''
        inicial = True
        for key in distancias:
            distancias[key] /= n[key]
            if inicial:
                minimo = distancias[key]
                claseMinima = key
                inicial = False

            if distancias[key] > minimo:
                minimo = distancias[key]
                claseMinima = key

        return claseMinima, distancias
    def desempateMinimo(self):
        distancias = {}
        n = {}
        for index in range(len(self.patrones)):
            if not (self.patrones[index].getClase() in distancias):
                distancias[self.patrones[index].getClase()] = 0
                n[self.patrones[index].getClase()] = 0
            distancias[self.patrones[index].getClase()] += self.patrones[index].getDistancia()
            n[self.patrones[index].getClase()] += 1
        minimo = 0
        claseMinima = ''
        inicial = True
        for key in distancias:
            distancias[key] /= n[key]
            if inicial:
                minimo = distancias[key]
                claseMinima = key
                inicial = False

            if distancias[key] < minimo:
                minimo = distancias[key]
                claseMinima = key

        return claseMinima, distancias

    def ordenarPatrones(self):
        if self.patrones is None:
            print('No hay patrones')
            return

        n = len(self.patrones) 
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if self.patrones[j].getDistancia() > self.patrones[j+1].getDistancia() : 
                    self.patrones[j], self.patrones[j+1] = self.patrones[j+1], self.patrones[j] 
            

    def setPatron(self, patron):
        self.patron = patron
    
    def setClases(self, clases):
        self.clases = clases
        self.calcularRepresentantes()

    def getPatronByIndex(self, index):
        return self.patrones[index]

    def calcularRepresentantes(self):
        representantes = {}
        for key in self.clases:
            representanteClase = []
            for patrones in self.clases[key]:
                suma = 0
                for x in patrones:
                    suma += x 

                suma = suma / len(patrones)
                representanteClase.append(suma)

            representantes[key] = representanteClase

        self.representantes = representantes
 
    def getRepresentantes(self):
        print('Representantes calculados:', self.representantes)
        return self.representantes

    def cityBlock(self):
        distancias = []
        distanciaMenor = 0
        clasePertenciente = 'c1'
        for key in self.representantes:
            #sumaDeCoordenada = 0
            sumatoria = 0
            for i in range(len(self.representantes[key])):
                sumatoria += abs(self.patron[i] - self.representantes[key][i])
            
            print('Distancia de {}: {}'.format(key, sumatoria))
            distancias.append(sumatoria)
            if key == 'c1':
                distanciaMenor = sumatoria

            if sumatoria < distanciaMenor:
                distanciaMenor = sumatoria
                clasePertenciente = key

        return clasePertenciente, distancias

    def ecuclidea(self):
        distancias = []
        distanciaMenor = 0
        clasePertenciente = 'c1'
        for key in self.representantes:
            #sumaDeCoordenada = 0
            sumatoria = 0
            for i in range(len(self.representantes[key])):
                sumatoria += abs(self.patron[i] - self.representantes[key][i])**2
            
            print('Distancia de {}: {}'.format(key, sumatoria))
            distancias.append(sumatoria)
            if key == 'c1':
                distanciaMenor = math.sqrt(sumatoria)
            if math.sqrt(sumatoria) < distanciaMenor:
                distanciaMenor = math.sqrt(sumatoria)
                clasePertenciente = key

        return clasePertenciente, distancias

    def infinito(self):
        distancias = []
        distanciaMenor = 0
        clasePertenciente = 'c1'
        for key in self.representantes:
            #sumaDeCoordenada = 0
            sumatoria = 0
            aux = 0
            for i in range(len(self.representantes[key])):
                sumatoria = abs(self.patron[i] - self.representantes[key][i])
                if sumatoria > aux : 
                    aux=sumatoria 
            print('Distancia de {}: {}'.format(key, sumatoria))
            distancias.append(sumatoria)
            if key == 'c1':
                distanciaMenor = aux
            if aux < distanciaMenor:
                distanciaMenor = aux
                clasePertenciente = key

        return clasePertenciente, distancias

    
        