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
            self.spinBox_salt.valueChanged.connect(self.addNoise)
            self.spinBox_pepper.valueChanged.connect(self.addNoise)
            self.pushButton_addNoise.setEnabled(False)
        else:
            self.spinBox_salt.valueChanged.disconnect()
            self.spinBox_pepper.valueChanged.disconnect()
            self.pushButton_addNoise.setEnabled(True)


    def openImage(self, filename):
        img = cv2.imread('images/'+filename+'.bmp',0)
        img = img > 0
        img = img.astype(int)
        return img

    def restartVocalImage(self):
        vocal = str(self.comboBox.currentText())
        self.currentVocalImage = self.openImage(vocal)
        self.showVocalImage(self.currentVocalImage)

    def addNoise(self):
        pepper = self.spinBox_pepper.value()
        salt = self.spinBox_salt.value()
        self.currentVocalImage = self.noise(self.currentVocalImage, salt, pepper)
        self.showVocalImage(self.currentVocalImage)
        
    def noise(self, img, salt, pepper):
        salt /= 100
        pepper /= 100
        height=img.shape[0]
        width=img.shape[1]  
        img_r=np.asarray(img.copy(),order="C")
        
        hw=height*width
        
        if salt>0 and salt<=1:
            npixels=int(float(hw)*salt)
            for i in range(npixels):
                x = np.random.randint(0,width,1)
                y = np.random.randint(0,height,1)
                img_r[y[0],x[0]]=1
                
            
        if pepper>0 and pepper<=1:
            npixels=int(float(hw)*pepper)
            for i in range(npixels):
                x = np.random.randint(0,width,1)
                y = np.random.randint(0,height,1)
                img_r[y[0],x[0]]=0
        
        return img_r

    def showVocalImage(self, currentVocalImage):
        img = copy.deepcopy(currentVocalImage)
        img = np.where(img > 0, 255, 0)
        img = img.astype(float)

        img = cv2.resize(img, (200,200), interpolation = cv2.INTER_AREA)
        cv2.imwrite('visualVocalImage.bmp', img)
        self.imagenVocal.setPixmap(QPixmap('visualVocalImage.bmp'))
        self.imagenVocal.setScaledContents(True)
    
   
        
    # def tabChange(self):
    #     if self.tabWidget.currentIndex() == 1:
    #         datos = self.getDataTable()
    #         print('getDataTable()==>',datos)
    #         patron = self.getPatronDesconocido()
    #         # self.clasificador.setPatronDesconcido(patron)
    #         self.clasificador.setPatrones(datos)
    #         # self.rellenarDatosOrdenados()
    #         if self.spinBoxDimensionPatron.value() == 2:
    #             if (not datos is None) and (not patron is None):
    #                 self.generarGrafico(datos, patron, 'graficoTodos')
    #                 # loading image 
    #                 self.pixmap = QPixmap('graficoTodos.png') 
    #                 # adding image to label 
    #                 self.imagenTodos.setPixmap(self.pixmap)
                    

    #                 self.generarGraficoFronteraDesicion(datos, patron, self.clasificador.getW(), self.clasificador.getB())
    #                 # loading image 
    #                 self.pixmap = QPixmap('graficoFrontera.png') 
    #                 # adding image to label 
    #                 self.imagenK.setPixmap(self.pixmap)

    #                 # self.clasificador.setClases(datos)
    #                 # self.generarGrafico(self.clasificador.getRepresentantes(), patron, 'graficoRepre')
    #                 # # loading image 
    #                 # self.pixmap = QPixmap('graficoRepre.png') 
    #                 # # adding image to label 
    #                 # self.imagenRepresentantes.setPixmap(self.pixmap)
    #             else:
    #                 self.imagenTodos.setText('Datos erroneos')
    #                 self.imagenRepresentantes.setText('Datos erroneos')

    #     if self.tabWidget.currentIndex() == 2:
    #         datos = self.getDataTable()
    #         patron = self.getPatronDesconocido()
    #         # self.clasificador.setPatronDesconcido(patron)
    #         self.clasificador.setPatrones(datos)
    #         if (not datos is None) and (not patron is None):
    #             self.generarGraficoEvolucionError(self.clasificador.getEpocas(), self.clasificador.getErrores())
    #             # loading image 
    #             self.pixmap = QPixmap('graficoError.png') 
    #             # adding image to label 
    #             self.imagenError.setPixmap(self.pixmap)

    #             self.setConfusionMatrix(self.clasificador.getConfusionMatrix())

    #         else:
    #             self.imagenTodos.setText('Datos erroneos')
    #             self.imagenRepresentantes.setText('Datos erroneos')

    def clasificarButton(self):
        maxR, minR = self.memoria.recuperar(self.currentVocalImage)
        # print('maxR={} minR={}'.format(maxR, minR))
        cadena = ''
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
        # print(cadena)
        self.labelRes.setText(cadena)

        self.label_Onehot.setText('Etiqueta(max):{}\nEtiqueta(min):{}'.format(maxR, minR))
    
    def __del__(self):
        pass
        #print('End exec')
        try:
            os.remove('visualVocalImage.bmp')
        except:
            print('No se genero grafico')
        #os.remove('histVerduras.png')

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()