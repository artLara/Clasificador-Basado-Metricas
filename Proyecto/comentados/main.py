from memoria_ui import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random
import time
import _thread

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap 
import math
import os 
import pyautogui
import cv2
import copy
from MemoriaAlphaBetaHetereo import MemoriaAlphaBetaHetereo

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.comboBox.currentIndexChanged.connect(self.restartVocalImage)
        self.checkBox_dynamicNoise.stateChanged.connect(self.dynamicNoise)
        self.pushButton_addNoise.clicked.connect(self.addNoise)
        self.pushButton_restartImage.clicked.connect(self.restartVocalImage)
        self.currentVocalImage = self.openImage('a')
        self.showVocalImage(self.currentVocalImage)
        self.memoria = MemoriaAlphaBetaHetereo()
        self.pushButtonClasificar.clicked.connect(self.clasificarButton)
        self.y = self.memoria.generarEtiquetasOnehot()

    def dynamicNoise(self):
        if self.checkBox_dynamicNoise.isChecked():
            # Si el ruido dinamico es activado se aplicara ruido cada vez que cambie el valor
            self.spinBox_salt.valueChanged.connect(self.addNoise)
            self.spinBox_pepper.valueChanged.connect(self.addNoise)
            self.pushButton_addNoise.setEnabled(False)
        else:
            self.spinBox_salt.valueChanged.disconnect()
            self.spinBox_pepper.valueChanged.disconnect()
            self.pushButton_addNoise.setEnabled(True)


    def openImage(self, filename):
        img = cv2.imread('images/'+filename+'.bmp',0) #Lectura en escala de grises
        #Binarizacion
        img = img > 0
        img = img.astype(int)
        return img

    def restartVocalImage(self):
        # Restablece la imagen a su forma original
        vocal = str(self.comboBox.currentText())#Obtiene la vocal seleccionada
        self.currentVocalImage = self.openImage(vocal)#Abre la imagen
        self.showVocalImage(self.currentVocalImage)#Muestra la imagen

    def addNoise(self):
        pepper = self.spinBox_pepper.value()# Obtiene el porcentaje del ruido pimienta
        salt = self.spinBox_salt.value()# Obtiene el porcentaje del ruido sal
        self.currentVocalImage = self.noise(self.currentVocalImage, salt, pepper)#Aplica ruido a la imagen
        self.showVocalImage(self.currentVocalImage)#Muestra la imagen con ruido
        
    def noise(self, img, salt, pepper):
        salt /= 100 #Normaliza el valor del ruido
        pepper /= 100 #Normaliza el valor del ruido
        height=img.shape[0] #Obtiene el alto de la imagen
        width=img.shape[1] #Obtiene el ancho de la imagen
        img_r=np.asarray(img.copy(),order="C") #Crea una copia de la imagen
        
        hw=height*width
        
        if salt>0 and salt<=1: #Verifica que el ruido sal este en el rango permitido
            npixels=int(float(hw)*salt) #Calcula el numero de pixeles a afectar
            for i in range(npixels):
                x = np.random.randint(0,width,1) #Obtiene la coordenada x aletoriamente
                y = np.random.randint(0,height,1) #Obtiene la coordenada y aletoriamente
                img_r[y[0],x[0]]=1 #Se altera el pixel agregando el ruido sal
                
            
        if pepper>0 and pepper<=1:#Verifica que el ruido sal este en el rango permitido
            npixels=int(float(hw)*pepper) #Calcula el numero de pixeles a afectar
            for i in range(npixels):
                x = np.random.randint(0,width,1) #Obtiene la coordenada x aletoriamente
                y = np.random.randint(0,height,1) #Obtiene la coordenada y aletoriamente
                img_r[y[0],x[0]]=0 #Se altera el pixel agregando el ruido pimienta
        
        return img_r

    def showVocalImage(self, currentVocalImage):
        img = copy.deepcopy(currentVocalImage) #Crea una copia de la imagen binaria
        img = np.where(img > 0, 255, 0) # Dado a que python despliega en escala de grises se cambian unos por 255.
        img = img.astype(float) # Casteo necesario para mostrar la imagen

        img = cv2.resize(img, (200,200), interpolation = cv2.INTER_AREA)# Agrandamos la imagen para mejor visualizacion
        cv2.imwrite('visualVocalImage.bmp', img) #Se genera la imagen
        #Se muestra en la interfaz grafica
        self.imagenVocal.setPixmap(QPixmap('visualVocalImage.bmp'))
        self.imagenVocal.setScaledContents(True)

    def clasificarButton(self):
        maxR, minR = self.memoria.recuperar(self.currentVocalImage) #Se recupera el valor
        cadena = ''

        #Mapeo del vector Y a la vocal correspondiente
        if (maxR==self.y[0]).all():
            cadena += 'Memoria max: a |'
        elif (maxR==self.y[1]).all():
            cadena += 'Memoria max: e |'
        elif (maxR==self.y[2]).all():
            cadena += 'Memoria max: i |'
        elif (maxR==self.y[3]).all():
            cadena += 'Memoria max: o |'
        elif (maxR==self.y[4]).all():
            cadena += 'Memoria max: u |'
        else:
            cadena += 'Memoria max: Sin clasificación |'

        if (minR==self.y[0]).all():
            cadena += ' Memoria min: a'
        elif (minR==self.y[1]).all():
            cadena += ' Memoria min: e'
        elif (minR==self.y[2]).all():
            cadena += ' Memoria min: i'
        elif (minR==self.y[3]).all():
            cadena += ' Memoria min: o'
        elif (minR==self.y[4]).all():
            cadena += ' Memoria min: u'
        else:
            cadena += ' Memoria min: Sin clasificación'
        self.labelRes.setText(cadena) #Muestra resultado en la interfaz gráfica
        self.label_Onehot.setText('Etiqueta(max):{}\nEtiqueta(min):{}'.format(maxR, minR)) #Muestra la etiqueta en la interfaz gráfica
    
    def __del__(self):
        #Remueve las imagen utilizada en la ejecución
        try:
            os.remove('visualVocalImage.bmp')
        except:
            print('No se genero grafico')        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()