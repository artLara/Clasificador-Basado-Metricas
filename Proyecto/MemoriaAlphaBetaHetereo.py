import numpy as np
import cv2
from scipy import stats as st

class MemoriaAlphaBetaHetereo():
    def __init__(self):
        self.M = np.zeros((5, 400), dtype=int)
        self.W = np.zeros((5, 400), dtype=int)
        self.y = self.generarEtiquetasOnehot()
        self.vocales = self.getVocales()
        self.entrenar()

    
    def getVocales(self):
        vocales = []
        vocales.append(self.openImage('a'))
        vocales.append(self.openImage('e'))
        vocales.append(self.openImage('i'))
        vocales.append(self.openImage('o'))
        vocales.append(self.openImage('u'))
        return vocales

    def generarEtiquetasOnehot(self):
        y = []
        #Onehot funciona bien para max
        # y.append(np.array([1,0,0,0,0]))#Para A 
        # y.append(np.array([1,0,1,1,1]))#Para E
        # y.append(np.array([0,0,1,0,0]))#Para I
        # y.append(np.array([0,0,0,1,0]))#Para O
        # y.append(np.array([0,0,0,0,1]))#Para U

        #Funciona bien para min
        # y.append(np.array([0,1,1,1,1]))#Para A 
        # y.append(np.array([1,0,1,1,1]))#Para E
        # y.append(np.array([1,1,0,1,1]))#Para I
        # y.append(np.array([1,1,1,0,1]))#Para O
        # y.append(np.array([1,1,1,1,0]))#Para U

        ## Efectiva pero no si se equivoca manda todo a la U en el tipo min
        y.append(np.array([1,0,0,0,0]))#Para A 
        y.append(np.array([1,1,0,0,0]))#Para E
        y.append(np.array([1,1,1,0,0]))#Para I
        y.append(np.array([1,1,1,1,0]))#Para O
        y.append(np.array([1,1,1,1,1]))#Para U

        ## Efectiva pero no si se equivoca manda todo a la U
        # y.append(np.array([1,0,0,0,0]))#Para A 
        # y.append(np.array([1,1,0,0,0]))#Para E
        # y.append(np.array([0,0,1,1,1]))#Para I
        # y.append(np.array([0,1,1,0,0]))#Para O
        # y.append(np.array([0,0,0,0,1]))#Para U
        return y

    def alpha(self, x, y):
        # print('==>x:',x)
        # print('==>y:',y)

        if y==0 and x==0:
            return 1
        elif y==1 and x==0:
            return 0
        elif y==0 and x==1:
            return 2
        elif y==1 and x==1:
            return 1

    def beta(self, x, y):
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
        matrices = []
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para A
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para E
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para I
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para O
        matrices.append(np.zeros((5, 400), dtype=int))#Matriz para U

        for k in range(len(self.vocales)):
            for i in range(self.y[0].shape[0]):
                for j in range(self.vocales[0].shape[0]):            
                    matrices[k][i,j] = self.alpha(self.y[k][i], self.vocales[k][j])

        return matrices

    def entrenar(self):
        matrices = self.calcularMatrices()
        for i in range(self.y[0].shape[0]):
            for j in range(self.vocales[0].shape[0]):
                self.M[i,j] = max(matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j])
                
                ## Minimo
                self.W[i,j] = min(matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j])
                
                #Promedio
                # self.W[i,j] = int(np.mean([matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j]]))
                #Moda
                # self.W[i,j] = int(st.mode([matrices[0][i,j], matrices[1][i,j], matrices[2][i,j], matrices[3][i,j], matrices[4][i,j]])[0][0])

        # Sumar a la vocal e (solo funciona e)
        # for i in range(self.y[0].shape[0]):
        #     for j in range(self.vocales[0].shape[0]):
        #         self.W[i,j] += matrices[1][i,j]
        #         if self.W[i,j] > 2:
        #             self.W[i,j]=2
        #      
        ## Resta a la vocal e
        # for i in range(self.y[0].shape[0]):
        #     for j in range(self.vocales[0].shape[0]):
        #         self.W[i,j] -= matrices[1][i,j]
        #         if self.W[i,j] < 0:
        #             self.W[i,j]=0

        # Poniendo solo la vocal e
        # self.W = matrices[1]
        # print('W={}'.format(self.W))
    def recuperar(self, img):
        img = img.flatten()
        # print('normal image', img)
        # img = img[::-1]
        # print('Flip image', img)

        recuperadoMax = np.zeros((5), dtype=int)
        recuperadoMin = np.zeros((5), dtype=int)

        for i in range(self.M.shape[0]):
            minimo = 2
            maximo = 0
            for j in range(img.shape[0]):
                valorBetaMin = self.beta(self.M[i,j], img[j])
                valorBetaMax = self.beta(self.W[i,j], img[j])

                if minimo > valorBetaMin:
                    minimo = valorBetaMin

                if maximo < valorBetaMax:
                    maximo = valorBetaMax
            
            recuperadoMax[i] = minimo
            recuperadoMin[i] = maximo

        return recuperadoMax, recuperadoMin

    def openImage(self, filename):
        img = cv2.imread('images/'+filename+'.bmp',0)
        img = img > 0
        img = img.astype(int)
        img = img.flatten()
        # img = img[::-1]
        return img


    