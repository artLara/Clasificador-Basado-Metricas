from clasificadorKNN_ui import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap 
import math
import os 
from clasificadorKNN import clasificadorKNN

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.pushButtonClasificar.clicked.connect(self.clasificarButton)
        self.spinBoxNumeroClases.valueChanged.connect(self.numeroClasesValueChange)
        self.spinBoxNumeroPatrones.valueChanged.connect(self.numeroPatronesValueChange)
        self.spinBoxDimensionPatron.valueChanged.connect(self.numeroClasesValueChange)
        self.spinBoxK.valueChanged.connect(self.kValueChange)

        self.tabWidget.currentChanged.connect(self.tabChange)
        self.clasificador = clasificadorKNN()
    

    def kValueChange(self):
        self.clasificador.setK(self.spinBoxK.value())
        
    def tabChange(self):
        if self.tabWidget.currentIndex() == 1:
            datos = self.getDataTable()
            print('getDataTable()==>',datos)
            patron = self.getPatronDesconocido()
            self.clasificador.setPatronDesconcido(patron)
            self.clasificador.setPatrones(datos)
            self.rellenarDatosOrdenados()
            if self.spinBoxDimensionPatron.value() == 2:
                if (not datos is None) and (not patron is None):
                    self.generarGrafico(datos, patron, 'graficoTodos')
                    # loading image 
                    self.pixmap = QPixmap('graficoTodos.png') 
                    # adding image to label 
                    self.imagenTodos.setPixmap(self.pixmap)
                            
                    self.generarGraficoK(datos, patron, self.clasificador.getPatronK().getDistancia())
                    # loading image 
                    self.pixmap = QPixmap('graficoK.png') 
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
        numeroClase = 1
        for i in range(self.spinBoxNumeroClases.value() * self.spinBoxDimensionPatron.value()):
            if i == countHeaderClass:
                headers.append('C' + str(numeroClase))
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
            clases['c'+ str(i+1)] = []
        
        countHeaderClass = 0
        numeroClase = 1
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

    def generarGrafico(self, datos, patron, nameFile):
        #plt.grid(color='black', linestyle='-', linewidth=2)
        if self.radioButtonDistanciaMinina.isChecked() and nameFile == 'graficoRepre':
            for i in datos:
                plt.plot([patron[0], datos[i][0]], [patron[1], patron[1]], color='k')
                plt.plot([datos[i][0], datos[i][0]], [patron[1], datos[i][1]], color='k')

        if self.radioButtonDistanciaMedia.isChecked() and nameFile == 'graficoRepre':
            for i in datos:
                plt.plot([patron[0], datos[i][0]], [patron[1], datos[i][1]], color='k')

        
        plt.scatter(patron[0], patron[1], label='Patron desconocido', marker='x')

        for i in datos:
            plt.scatter(datos[i][0], datos[i][1], label=i)

        plt.legend(loc="lower right")
        plt.grid(linestyle='--')
        plt.savefig(nameFile + '.png', dpi=75)
        plt.cla()
        plt.clf()

    def generarGraficoK(self, datos, patron, radio=0):
        
        ##############Graficar patron desconocido
        plt.scatter(patron[0], patron[1], label='Patron desconocido', marker='x')

        ##############Graficar circunferencia 
        if radio == 0:
            try:
                radio = math.sqrt((patron[0] - datos['c1'][0][0])**2 + (patron[1] - datos['c1'][1][0])**2)

            except:
                #TO DO
                pass

        radio += 0.1
        theta = np.linspace(0, 2*np.pi, 100)
        x1 = radio * np.cos(theta) + patron[0]
        x2 = radio * np.sin(theta) + patron[1]
        plt.plot(x1, x2)
        
        #############Graficar puntos
        for i in datos:
            plt.scatter(datos[i][0], datos[i][1], label=i)
        

        plt.legend(loc="lower right")
        plt.grid(linestyle='--')
        plt.savefig('graficoK' + '.png', dpi=75)
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
        className = 'Seleccione un clasificador'

        datos = self.getDataTable()
        patron = self.getPatronDesconocido()
        if (not datos is None) and (not patron is None):
            self.clasificador.setPatronDesconcido(patron)
            self.clasificador.setPatrones(datos)
            self.clasificador.setK(self.clasificador.k%len(self.clasificador.patrones));

            if self.radioButtonDistanciaMinina.isChecked():
                clasificacion, patronesMinimos = self.clasificador.desempateMinimo()
                self.labelRes.setText('Clasificado en ' + clasificacion)
                self.setDesempateTable(patronesMinimos)

            elif self.radioButtonDistanciaMedia.isChecked():
                clasificacion, patronesMinimos = self.clasificador.desempateMedia()
                self.labelRes.setText('Clasificado en ' + clasificacion)
                self.setDesempateTable(patronesMinimos)

            elif self.radioButtonPesado.isChecked():
                clasificacion, patronesMinimos = self.clasificador.desempatePesos()
                self.labelRes.setText('Clasificado en ' + clasificacion)
                self.setDesempateTable(patronesMinimos)

            else:
                self.labelRes.setText(className)            

        else:
            self.labelRes.setText('Datos erroneos')

    
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