# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoria_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 727)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 536, 593))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 512, 359))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.imagenVocal = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.imagenVocal.setText("")
        self.imagenVocal.setObjectName("imagenVocal")
        self.gridLayout_7.addWidget(self.imagenVocal, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 5, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_6.addWidget(self.spinBox_2, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 3, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_6.addWidget(self.spinBox, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 1, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 1, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButtonClasificar = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonClasificar.setFont(font)
        self.pushButtonClasificar.setObjectName("pushButtonClasificar")
        self.verticalLayout_2.addWidget(self.pushButtonClasificar)
        self.labelRes = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelRes.setFont(font)
        self.labelRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRes.setObjectName("labelRes")
        self.verticalLayout_2.addWidget(self.labelRes)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 536, 593))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.labelInformation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelInformation.setFont(font)
        self.labelInformation.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInformation.setObjectName("labelInformation")
        self.gridLayout_4.addWidget(self.labelInformation, 0, 0, 1, 1)
        self.imagenK = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagenK.setText("")
        self.imagenK.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenK.setObjectName("imagenK")
        self.gridLayout_4.addWidget(self.imagenK, 4, 0, 1, 1)
        self.imagenTodos = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagenTodos.setText("")
        self.imagenTodos.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenTodos.setObjectName("imagenTodos")
        self.gridLayout_4.addWidget(self.imagenTodos, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 536, 593))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.imagenError = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.imagenError.setText("")
        self.imagenError.setObjectName("imagenError")
        self.verticalLayout_3.addWidget(self.imagenError)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.tableWidgetConfusionMatriz = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidgetConfusionMatriz.setObjectName("tableWidgetConfusionMatriz")
        self.tableWidgetConfusionMatriz.setColumnCount(0)
        self.tableWidgetConfusionMatriz.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidgetConfusionMatriz)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 536, 593))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imagePaisaje = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.imagePaisaje.setText("")
        self.imagePaisaje.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePaisaje.setObjectName("imagePaisaje")
        self.verticalLayout_4.addWidget(self.imagePaisaje)
        self.scrollArea_8 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_6)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 512, 237))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonMouse = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        self.radioButtonMouse.setObjectName("radioButtonMouse")
        self.horizontalLayout_4.addWidget(self.radioButtonMouse)
        self.radioButtonRGB = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_8)
        self.radioButtonRGB.setObjectName("radioButtonRGB")
        self.horizontalLayout_4.addWidget(self.radioButtonRGB)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_4.addWidget(self.scrollArea_8)
        self.scrollArea_7 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_6)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 512, 237))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.spinBoxR = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinBoxR.setMaximum(255)
        self.spinBoxR.setObjectName("spinBoxR")
        self.horizontalLayout_2.addWidget(self.spinBoxR)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.spinBoxG = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinBoxG.setMaximum(255)
        self.spinBoxG.setObjectName("spinBoxG")
        self.horizontalLayout_2.addWidget(self.spinBoxG)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.spinBoxB = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_7)
        self.spinBoxB.setMaximum(255)
        self.spinBoxB.setObjectName("spinBoxB")
        self.horizontalLayout_2.addWidget(self.spinBoxB)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_4.addWidget(self.scrollArea_7)
        self.pushButtonEstatico = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButtonEstatico.setEnabled(False)
        self.pushButtonEstatico.setObjectName("pushButtonEstatico")
        self.verticalLayout_4.addWidget(self.pushButtonEstatico)
        self.labelResPaisaje = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelResPaisaje.setFont(font)
        self.labelResPaisaje.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResPaisaje.setObjectName("labelResPaisaje")
        self.verticalLayout_4.addWidget(self.labelResPaisaje)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_5.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Memoria Alpha-Beta Heteroasosiativa"))
        self.comboBox.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox.setItemText(1, _translate("MainWindow", "e"))
        self.comboBox.setItemText(2, _translate("MainWindow", "i"))
        self.comboBox.setItemText(3, _translate("MainWindow", "o"))
        self.comboBox.setItemText(4, _translate("MainWindow", "u"))
        self.label_2.setText(_translate("MainWindow", "Añadir ruido"))
        self.label_8.setText(_translate("MainWindow", "Ruido sustractivo"))
        self.label_7.setText(_translate("MainWindow", "%"))
        self.label_9.setText(_translate("MainWindow", "%"))
        self.label_3.setText(_translate("MainWindow", "Ruido aditivo"))
        self.pushButton.setText(_translate("MainWindow", "Entrenar"))
        self.pushButtonClasificar.setText(_translate("MainWindow", "Clasificar"))
        self.labelRes.setText(_translate("MainWindow", "Resultado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clasificar"))
        self.label_5.setText(_translate("MainWindow", "Frontera de desición"))
        self.labelInformation.setText(_translate("MainWindow", "Información"))
        self.label_4.setText(_translate("MainWindow", "Gráfico de todos los puntos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Información"))
        self.label_6.setText(_translate("MainWindow", "Evolución del error"))
        self.label_10.setText(_translate("MainWindow", "Matriz de confusión"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Entrenamiento"))
        self.radioButtonMouse.setText(_translate("MainWindow", "Mouse"))
        self.radioButtonRGB.setText(_translate("MainWindow", "Valor estático"))
        self.label_15.setText(_translate("MainWindow", "R"))
        self.label_16.setText(_translate("MainWindow", "G"))
        self.label_17.setText(_translate("MainWindow", "B"))
        self.pushButtonEstatico.setText(_translate("MainWindow", "Clasificar valor estático"))
        self.labelResPaisaje.setText(_translate("MainWindow", "Resultado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Paisaje"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
