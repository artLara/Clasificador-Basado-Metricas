import math
from Patron import *

class Neurona():
    def __init__(self):
        self.patron = None
        self.patronDesconocido = None
        self.clases = None
        self.representantes = []
        self.patrones = None
        self.w = None
        self.b = None
        self.errores = None
        self.epocas = None
        self.maxEpoch=1
        self.lr = 0.001

    def getW(self):
        return self.w

    def getB(self):
        return self.b

    def getErrores(self):
        return self.errores

    def getEpocas(self):
        return self.epocas

    def setPatrones(self, data):
        self.patrones = []
        for key in data:
            print('Clase:', key)
            for index in range(len(data[key][0])):
                patron = Patron()
                patron.setClase(key)
                print('indice=', index)
                listaCaracteristicas=[]
                for listaPatrones in data[key]:
                    print('Carcateristicas agregada: ', listaPatrones[index])
                    listaCaracteristicas.append([listaPatrones[index]])
                
                patron.setCaracteristicas(listaCaracteristicas)
                self.patrones.append(patron)

        for p in self.patrones:
            print('=========')
            print(p.getClase())
            print(p.getCaracteristicas())

        self.inicializarW(len(self.patrones[0].getCaracteristicas()))
        self.inicializarB()
        print('w=',self.w)
        print('b=',self.b)
        print('Number class', self.patrones[0].getNumberClass())
        self.train()

    def inicializarW(self, dim):
        self.w = np.random.rand(dim,1) * 0.01

    def inicializarB(self):
        self.b = 1 #np.random.rand(1)

    def setMaxEpoch(self, maxEpoch):
        self.maxEpoch = maxEpoch

    def setLearningRate(self, learningRate):
        self.lr = learningRate

    def hardlim(self, x):
        if x >= 0:
            x = 1
        else:
            x=0
        return x  

    def train(self):
        self.errores = []
        self.epocas = []
        epoca = 1
        while True:
            errorGeneral = 0
            for p in self.patrones:
                a = self.hardlim(np.dot(self.w.transpose(),p.caracteristicas) + self.b)
                error = p.getNumberClass() - a
                self.w = self.w + error * p.caracteristicas
                self.b = self.b + error
                errorGeneral += abs(error)
                print('>>>>Epoca ', epoca,'<<<<')
                print('a=',a)
                print('Error=',error)
                print('w=',self.w)
                print('b=',self.b)


            self.errores.append(errorGeneral)
            self.epocas.append(epoca)
            epoca += 1
            print('Errro general=', errorGeneral)
            if errorGeneral == 0 or epoca>=self.maxEpoch:
                break


    def propagarHaciaAdelante(self, desconocido):
        a = self.hardlim(np.dot(self.w.transpose(),desconocido.caracteristicas) + self.b)
        return a

    def setPatronDesconcido(self, carcateristicas):
        patron = Patron()
        listaCaracteristicas=[]
        for carcateristica in carcateristicas:
            listaCaracteristicas.append(carcateristica)

        self.patronDesconocido = patron

    def getConfusionMatrix(self):
        matrix = {'pred0_0':0, 'pred1_1':0, 'pred1_0':0, 'pred0_1':0}
        for p in self.patrones:
            a = self.hardlim(np.dot(self.w.transpose(),p.caracteristicas) + self.b)
            matrix['pred'+str(a)+'_'+str(p.getNumberClass())] += 1

        return matrix
    #######Desempate distancia media
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

    #######Desempate pesado de casos
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
            if inicial:
                minimo = distancias[key]
                claseMinima = key
                inicial = False

            if distancias[key] > minimo:
                minimo = distancias[key]
                claseMinima = key

        return claseMinima, distancias

    #######Desempate distancia minima
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
        