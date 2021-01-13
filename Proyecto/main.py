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
# from Neurona import Neurona
# from Patron import Patron


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.comboBox.currentIndexChanged.connect(self.vocalChage)
        self.imagenVocal.setPixmap(QPixmap('images/a.bmp'))
        # self.pushButtonClasificar.clicked.connect(self.clasificarButton)
        # self.pushButtonEstatico.clicked.connect(self.clasificarPaisajeButton)
        # self.spinBoxNumeroClases.valueChanged.connect(self.numeroClasesValueChange)
        # self.spinBoxNumeroPatrones.valueChanged.connect(self.numeroPatronesValueChange)
        # self.spinBoxDimensionPatron.valueChanged.connect(self.numeroClasesValueChange)
        # self.spinBoxEpocas.valueChanged.connect(self.maxEpochValueChange)
        # self.doubleSpinBoxLearningRate.valueChanged.connect(self.lrValueChange)
        # self.doubleSpinBoxError.valueChanged.connect(self.errorValueChange)
        # self.imagePaisaje.setPixmap(QPixmap('paisaje.png'))
        # self.radioButtonMouse.toggled.connect(self.mouseSelected)
        # self.radioButtonRGB.toggled.connect(self.staticValue)

        
        # self.tabWidget.currentChanged.connect(self.tabChange)
        # self.clasificador = Neurona()
        # self.clasificadorPaisaje = Neurona()
        # # self.clasificadorPaisaje.w = np.array([[-0.006],[-0.0086],[0.0118]])
        # # self.clasificadorPaisaje.b = 0
        # self.clasificadorPaisaje.w = np.array([[0.08274324],[-0.15992965],[0.17016709]])
        # self.clasificadorPaisaje.b = 0.72796389

    def vocalChage(self):
        print('hola')

    def staticValue(self):
        if self.radioButtonRGB.isChecked():
            self.pushButtonEstatico.setEnabled(True)

    def mouseSelected(self):
        if self.radioButtonMouse.isChecked():
            self.pushButtonEstatico.setEnabled(False)
            # _thread.start_new_thread(self.getRGBbyMouse,())
            try:
                _thread.start_new_thread(self.getRGBbyMouse,())
            except:
                print('Error en thread')
        
    def getRGBbyMouse(self):
        while True:
            x, y = pyautogui.position()
            rgb = pyautogui.pixel(x, y)
            self.spinBoxR.setValue(rgb[0])
            self.spinBoxG.setValue(rgb[1])
            self.spinBoxB.setValue(rgb[2])

            patronDesconocido = Patron()
            listaCaracteristicas=[]
            listaCaracteristicas.append([rgb[0]])
            listaCaracteristicas.append([rgb[1]])
            listaCaracteristicas.append([rgb[2]])
            patronDesconocido.setCaracteristicas(listaCaracteristicas)
            clasificacion = self.clasificadorPaisaje.propagarHaciaAdelante(patronDesconocido)
            if clasificacion == 0:
                self.labelResPaisaje.setText('Clasificado en Zona boscosa')
            else:
                self.labelResPaisaje.setText('Clasificado en Cielo azul')


            if not self.radioButtonMouse.isChecked():
                break
            time.sleep(0.1)


    def lrValueChange(self):
        self.clasificador.setLearningRate(self.doubleSpinBoxLearningRate.value())

    def errorValueChange(self):
        self.clasificador.setErrorMinimo(self.doubleSpinBoxError.value())
    
    def maxEpochValueChange(self):
        self.clasificador.setMaxEpoch(self.spinBoxEpocas.value())
        
    def tabChange(self):
        if self.tabWidget.currentIndex() == 1:
            datos = self.getDataTable()
            print('getDataTable()==>',datos)
            patron = self.getPatronDesconocido()
            # self.clasificador.setPatronDesconcido(patron)
            self.clasificador.setPatrones(datos)
            # self.rellenarDatosOrdenados()
            if self.spinBoxDimensionPatron.value() == 2:
                if (not datos is None) and (not patron is None):
                    self.generarGrafico(datos, patron, 'graficoTodos')
                    # loading image 
                    self.pixmap = QPixmap('graficoTodos.png') 
                    # adding image to label 
                    self.imagenTodos.setPixmap(self.pixmap)
                    

                    self.generarGraficoFronteraDesicion(datos, patron, self.clasificador.getW(), self.clasificador.getB())
                    # loading image 
                    self.pixmap = QPixmap('graficoFrontera.png') 
                    # adding image to label 
                    self.imagenK.setPixmap(self.pixmap)

                    # self.clasificador.setClases(datos)
                    # self.generarGrafico(self.clasificador.getRepresentantes(), patron, 'graficoRepre')
                    # # loading image 
                    # self.pixmap = QPixmap('graficoRepre.png') 
                    # # adding image to label 
                    # self.imagenRepresentantes.setPixmap(self.pixmap)
                else:
                    self.imagenTodos.setText('Datos erroneos')
                    self.imagenRepresentantes.setText('Datos erroneos')

        if self.tabWidget.currentIndex() == 2:
            datos = self.getDataTable()
            patron = self.getPatronDesconocido()
            # self.clasificador.setPatronDesconcido(patron)
            self.clasificador.setPatrones(datos)
            if (not datos is None) and (not patron is None):
                self.generarGraficoEvolucionError(self.clasificador.getEpocas(), self.clasificador.getErrores())
                # loading image 
                self.pixmap = QPixmap('graficoError.png') 
                # adding image to label 
                self.imagenError.setPixmap(self.pixmap)

                self.setConfusionMatrix(self.clasificador.getConfusionMatrix())

            else:
                self.imagenTodos.setText('Datos erroneos')
                self.imagenRepresentantes.setText('Datos erroneos')


    def rellenarDatosOrdenados(self):
        self.tableWidgetCasosOrdenados.setColumnCount(2 + self.spinBoxDimensionPatron.value())
        #Se agregan los nombres a las filas
        headers = ['Clase']
        
        # numeroCoord = 1
        for i in range(self.spinBoxDimensionPatron.value()):
            headers.append('Coord' + str(i+1))
        
        headers.append('Distancia')
        self.tableWidgetCasosOrdenados.setHorizontalHeaderLabels(headers)
        self.tableWidgetCasosOrdenados.setRowCount(self.spinBoxK.value())

        #print('Numero de patrones=', self.spinBoxK.value())
        for i in range(self.spinBoxK.value()):#Rows
            #for j in range(2 + self.spinBoxDimensionPatron.value()):#Coulumns
            self.tableWidgetCasosOrdenados.setItem(i, 0, QTableWidgetItem(str(self.clasificador.getPatronByIndex(i).getClase())))
            for coor in range(self.spinBoxDimensionPatron.value()):
                c = str(self.clasificador.getPatronByIndex(i).getCaracteristicaIndex(coor))
                self.tableWidgetCasosOrdenados.setItem(i, coor+1, QTableWidgetItem(c))
            
            self.tableWidgetCasosOrdenados.setItem(i, coor+2, QTableWidgetItem('{:.2f}'.format(self.clasificador.getPatronByIndex(i).getDistancia())))
            

    def numeroClasesValueChange(self):
        #Se dan el numero de columnas solicitadas
        self.tableDatos.setColumnCount(self.spinBoxNumeroClases.value() * self.spinBoxDimensionPatron.value())
        #Se agregan los nombres a las filas
        headers = []
        countHeaderClass = 0
        numeroClase = 0
        for i in range(self.spinBoxNumeroClases.value() * self.spinBoxDimensionPatron.value()):
            if i == countHeaderClass:
                headers.append('C ' + str(numeroClase))
                countHeaderClass += self.spinBoxDimensionPatron.value()
                numeroClase += 1
            else:
                headers.append(' ')
            
        self.tableDatos.setHorizontalHeaderLabels(headers)
        self.rellenarTabla()

        self.tablePatronDesconocido.setColumnCount(self.spinBoxDimensionPatron.value())
        self.rellenarTablaPatronDesconocido()

    def numeroPatronesValueChange(self):
        #Se dan el numero de filas solicitadas
        self.tableDatos.setRowCount(self.spinBoxNumeroPatrones.value())
        #Se agregan los nombres a las filas
        rowsNames = []
        for i in range(self.spinBoxNumeroPatrones.value()):
            rowsNames.append('x' + str(i + 1))

        self.tableDatos.setVerticalHeaderLabels(rowsNames)
        self.rellenarTabla()

    def rellenarTabla(self):
        for i in range(self.spinBoxNumeroPatrones.value()):#Rows
            for j in range(self.spinBoxNumeroClases.value() * self.spinBoxDimensionPatron.value()):#Coulumns
                item = self.tableDatos.takeItem(i, j)
                if item is None:  
                    self.tableDatos.setItem(i, j, QTableWidgetItem('N'))
                else: 
                    self.tableDatos.setItem(i, j, item)
    
    def rellenarTablaPatronDesconocido(self):
        for j in range(self.spinBoxDimensionPatron.value()):#Coulumns
            item = self.tablePatronDesconocido.takeItem(0, j)
            #print('Item=', item)
            if item is None:
                self.tablePatronDesconocido.setItem(0, j, QTableWidgetItem('0'))
            else: 
                self.tablePatronDesconocido.setItem(0, j, item)

    def getDataTable(self):
        clases = {}
        for i in range(self.spinBoxNumeroClases.value()):
            clases['c'+ str(i)] = []
        
        countHeaderClass = 0
        numeroClase = 0
        key = ''
        for j in range(self.spinBoxNumeroClases.value() * self.spinBoxDimensionPatron.value()):#Coulumns(Clases)
            if j == countHeaderClass:
                key = 'c' + str(numeroClase) 
                countHeaderClass += self.spinBoxDimensionPatron.value()
                numeroClase += 1
                
            listaPatronesColumna = []
            for i in range(self.spinBoxNumeroPatrones.value()):#Rows(Patrones)
                dato = self.tableDatos.item(i, j).text()
                if dato == 'N':
                    continue

                if self.isNumber(dato):
                    listaPatronesColumna.append(float(dato))
                
                else:
                    return None

            clases[key].append(listaPatronesColumna)

        return clases

    def getPatronDesconocido(self):
        patron = []
        for j in range(self.spinBoxDimensionPatron.value()):#Coulumns(Clases)
            dato = self.tablePatronDesconocido.item(0, j).text()
            if self.isNumber(dato):
                patron.append(float(dato))
            else:
                return None
        
        return patron
        

    def isNumber(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def setConfusionMatrix(self, matrix):
        print(matrix)
        self.tableWidgetConfusionMatriz.setColumnCount(2)
        self.tableWidgetConfusionMatriz.setRowCount(2)
        #Se agregan los nombres a las filas
        headers = ['Clase 0', 'Clase 1']
        self.tableWidgetConfusionMatriz.setHorizontalHeaderLabels(headers)

        #Se agregan los nombres a las filas
        rowsNames = ['Clasificado 0', 'Clasificado 1']
        self.tableWidgetConfusionMatriz.setVerticalHeaderLabels(rowsNames)

        self.tableWidgetConfusionMatriz.setItem(0, 0, QTableWidgetItem(str(matrix['pred0_0'])))
        self.tableWidgetConfusionMatriz.setItem(0, 1, QTableWidgetItem(str(matrix['pred0_1'])))
        self.tableWidgetConfusionMatriz.setItem(1, 0, QTableWidgetItem(str(matrix['pred1_0'])))
        self.tableWidgetConfusionMatriz.setItem(1, 1, QTableWidgetItem(str(matrix['pred1_1'])))

        
        
    def generarGraficoEvolucionError(self, epocas, error):
        plt.plot(epocas, error)

        plt.xlabel("Epocas")
        plt.ylabel("Error")
        plt.legend()
        plt.grid(linestyle='--')
        plt.savefig('graficoError' + '.png', dpi=75)
        plt.cla()
        plt.clf()

    def generarGrafico(self, datos, patron, nameFile):
        plt.scatter(patron[0], patron[1], label='Patron desconocido', marker='x')

        for i in datos:
            plt.scatter(datos[i][0], datos[i][1], label=i)

        plt.legend()
        plt.grid(linestyle='--')
        plt.savefig(nameFile + '.png', dpi=75)
        plt.cla()
        plt.clf()

    def generarGraficoFronteraDesicion(self, datos, patron, w, b):
        
        ##############Graficar patron desconocido
        plt.scatter(patron[0], patron[1], label='Patron desconocido', marker='x')
        
        #############Graficar puntos
        max_x = patron[0]
        min_x = patron[0]
        for i in datos:
            plt.scatter(datos[i][0], datos[i][1], label=i)
            if max_x < max(datos[i][0]):
                max_x = max(datos[i][0])

            if min_x > min(datos[i][0]):
                min_x = min(datos[i][0])

        ## Frontera de descion
        x, y = [min_x, max_x], [self.getY(w, b, min_x), self.getY(w, b, max_x)]
        plt.plot(x, y)

        plt.legend()
        plt.grid(linestyle='--')
        plt.savefig('graficoFrontera' + '.png', dpi=75)
        plt.cla()
        plt.clf()
    
    # def generarGraficoRepresentantes(self, datos, patron, nameFile):
    #     #plt.grid(color='black', linestyle='-', linewidth=2)
        
    #     if self.radioButtonCityBlock.isChecked():
    #         for clase in datos:    
    #             plt.plot([patron[0], datos], y_values)

    #     plt.scatter(patron[0], patron[1], label='Patron desconocido')

    #     for clase in datos: 
    #         plt.scatter(datos[0], datos[1], label=clase)

    #     plt.legend(loc="upper left")
    #     plt.savefig(nameFile + '.png', dpi=75)
    #     plt.cla()
    #     plt.clf()

    def getY(self, w, b, max_x):
        m = -(w[0][0]/w[1][0])
        return m*max_x - b/w[1][0]

    def setDistancias(self, distancias):
        cadena = ''
        numeroClase = 1
        for i in distancias:
            cadena += 'C' + str(numeroClase) + ': ' + str(i) + '\n'
            numeroClase += 1 

        self.labelDistancias.setText(cadena)
                        
    def setDesempateTable(self, distancias):
        self.tableWidgetDesempate.setColumnCount(2)
        #Se agregan los nombres a las filas
        headers = ['Clase', 'Distancia']
        
        self.tableWidgetDesempate.setHorizontalHeaderLabels(headers)
        self.tableWidgetDesempate.setRowCount(self.spinBoxNumeroClases.value())

        rowCount = 0
        for key in distancias:
            self.tableWidgetDesempate.setItem(rowCount, 0, QTableWidgetItem(key))
            self.tableWidgetDesempate.setItem(rowCount, 1, QTableWidgetItem('{:.2f}'.format(distancias[key])))
            rowCount += 1

    def clasificarButton(self):
        datos = self.getDataTable()
        patronCaracteristicas = self.getPatronDesconocido()
        if (not datos is None) and (not patronCaracteristicas is None):
            self.clasificador.setPatrones(datos)
            patronDesconocido = Patron()
            listaCaracteristicas=[]
            for caracteristica in patronCaracteristicas:
                listaCaracteristicas.append([caracteristica])

            patronDesconocido.setCaracteristicas(listaCaracteristicas)
            clasificacion = self.clasificador.propagarHaciaAdelante(patronDesconocido)
            self.labelRes.setText('Clasificado en C' + str(clasificacion))
            
        else:
            self.labelRes.setText('Datos erroneos')

    def clasificarPaisajeButton(self):
        patronDesconocido = Patron()
        listaCaracteristicas=[]
        listaCaracteristicas.append([self.spinBoxR.value()])
        listaCaracteristicas.append([self.spinBoxG.value()])
        listaCaracteristicas.append([self.spinBoxB.value()])
        patronDesconocido.setCaracteristicas(listaCaracteristicas)
        clasificacion = self.clasificadorPaisaje.propagarHaciaAdelante(patronDesconocido)
        if clasificacion == 0:
            self.labelResPaisaje.setText('Clasificado en Zona boscosa')
        else:
            self.labelResPaisaje.setText('Clasificado en Cielo azul')

    
    def __del__(self):
        pass
        #print('End exec')
        try:
            os.remove('graficoTodos.png')
            os.remove('graficoRepre.png')
        except:
            print('No se genero grafico')
        #os.remove('histVerduras.png')

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()