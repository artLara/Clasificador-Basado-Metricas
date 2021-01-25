import numpy as np
import cv2
from scipy import stats as st

class MemoriaAlphaBetaHetereo():
    def __init__(self):
        self.M = np.zeros((5, 400), dtype=int) #Inicializar con ceros matriz M
        self.W = np.zeros((5, 400), dtype=int) #Inicializar con ceros matriz W
        self.y = self.generarEtiquetasOnehot() #Inicializar etiquetas
        self.vocales = self.getVocales()
        self.entrenar() #Entrenameinto de la memoria

    
    def getVocales(self):
        #Las imagenes de las vocales son almacenadas en el arreglo
        vocales = []
        vocales.append(self.openImage('a'))
        vocales.append(self.openImage('e'))
        vocales.append(self.openImage('i'))
        vocales.append(self.openImage('o'))
        vocales.append(self.openImage('u'))
        return vocales

    def generarEtiquetasOnehot(self):
        y = []
        ## Efectiva pero no si se equivoca manda todo a la U en el tipo min
        y.append(np.array([1,0,0,0,0]))#Para A 
        y.append(np.array([1,1,0,0,0]))#Para E
        y.append(np.array([1,1,1,0,0]))#Para I
        y.append(np.array([1,1,1,1,0]))#Para O
        y.append(np.array([1,1,1,1,1]))#Para U
        return y

    def alpha(self, x, y):
        # Implementación de operación alpha
        if y==0 and x==0:
            return 1
        elif y==1 and x==0:
            return 0
        elif y==0 and x==1:
            return 2
        elif y==1 and x==1:
            return 1

    def beta(self, x, y):
        # Implementación de operación beta
        if y==0 and x==0:
            return 0
        elif y==1 and x==0:
            return 0
        elif y==0 and x==1:
            return 0
        elif y==1 and x==1:
            return 1
        elif y==0 and x==2:
            return 1
        elif y==1 and x==2:
            return 1

    def calcularMatrices(self):
        #Inicializacion de matrices con ceros
        matrices = []
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para A
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para E
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para I
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para O
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para U

        #Calculo de YxX
        for k in range(len(self.vocales)):
            for i in range(self.y[0].shape[0]):
                for j in range(self.vocales[0].shape[0]):            
                    matrices[k][i,j] = self.alpha(self.y[k][i], self.vocales[k][j])

        return matrices

    def entrenar(self):
        matrices = self.calcularMatrices() #Calculo de YxX
        for i in range(self.y[0].shape[0]):
            for j in range(self.vocales[0].shape[0]):
                #Operacion max
                self.M[i,j] = max(matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j])
                #Operacion min
                self.W[i,j] = min(matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j])
                
    def recuperar(self, img):
        img = img.flatten() #Aplanado de imagen

        recuperadoMax = np.zeros((5), dtype=int) #Inicalizacion de vector recuperada tipo max
        recuperadoMin = np.zeros((5), dtype=int) #Inicalizacion de vector recuperada tipo min

        #Recuperacion
        for i in range(self.M.shape[0]):
            minimo = 2 #El mayor minimo que puede existir es 2
            maximo = 0 #El menor maximo que puede existir es 0
            for j in range(img.shape[0]):
                valorBetaMin = self.beta(self.M[i,j], img[j]) #Calculo de operacion beta
                valorBetaMax = self.beta(self.W[i,j], img[j]) #Calculo de operacion beta

                #Calculando el maximo y minimo
                if minimo > valorBetaMin:
                    minimo = valorBetaMin

                if maximo < valorBetaMax:
                    maximo = valorBetaMax
            
            recuperadoMax[i] = minimo #Asignacion al vector de salida tipo max
            recuperadoMin[i] = maximo #Asignacion al vector de salida tipo min

        return recuperadoMax, recuperadoMin

    def openImage(self, filename):
        img = cv2.imread('images/'+filename+'.bmp',0) #Lectura en escala de grises
        #Binarización
        img = img > 0 
        img = img.astype(int)
        #Aplanado de la imagen
        img = img.flatten()
        return img
    