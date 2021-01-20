from PyQt5 import QtWidgets

from menu import Ui_Form  # importing our generated file

import sys
import threading
import time
import os

def fun_threading(a):
    text="Hola\nReconocimiento de patrones\nEstrada Bernal José Bryan\nLara Casares Jaime Arturo"
    i=0 
    flag = True
    while True:
        if i<=len(text) and flag:
            i+=1
        if flag==False: 
            i-=1
        if i == len(text):
            flag=False
        if i == 0: 
            flag=True
        a.setText(text[:i]+'_')
        time.sleep(.2)

def funcOpen(a):
    if a==1: 
        t = threading.Thread(target=os.system, args=("python3 Clasificador-KNN/main.py",))
    if a==2:
        t = threading.Thread(target=os.system, args=("python3 Neurona/main.py",))
    if a==3:
        t = threading.Thread(target=os.system, args=("python3 Metricas/main.py",))
    if a==4:
        t = threading.Thread(target=os.system, args=("python3 Proyecto/main.py",))

    t.daemon=True
    t.start()
    


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
t = threading.Thread(target=fun_threading, args=(ui.lblNames,))
t.daemon= True
t.start()
ui.btnKNn.clicked.connect(lambda : funcOpen(1))
ui.btnMetricas.clicked.connect(lambda : funcOpen(3))
ui.btnProyecto.clicked.connect(lambda : funcOpen(4))
ui.btnNeurona.clicked.connect(lambda : funcOpen(2))
Form.show()
sys.exit(app.exec_())