
import sys
from zaber_motion import Library
# PREDEFINITIONS REQUIRED FOR STAGES
Library.enable_device_db_store()
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)
from PyQt5.QtCore import QTime, QTimer
###TEST ONLY
from random import randint
###TEST ONLY

class Scanning_Probe(QMainWindow):
    '''Here I am describbing how my window is being made and how all classes are built'''
    def __init__(self, position):
        super().__init__()
        self.position = 0
        self.initUI()

    def initUI(self):
        '''Here I initialise all window and display'''
        self.lcd = QLCDNumber(self)
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        self.setLayout(layout)
        btn1 = QPushButton("Run the Osilla Measurement", self)
        btn1.setGeometry(100, 50, 200, 100)
        btn2 = QPushButton("Run the Zaber Movement", self)
        btn2.setGeometry(100, 150, 200, 100)
        btn3 = QPushButton("Home position", self)
        btn3.setGeometry(100, 250, 200, 100)
        btn1.clicked.connect(self.osilla_run)
        btn2.clicked.connect(self.zaber_run)
        btn3.clicked.connect(self.handleButton)
        #lcd.display(self.osilla_run())
        self.lcd.setGeometry(300, 300, 250, 150)
        self.statusBar()
        self.setGeometry(300, 300, 650, 550)
        self.setWindowTitle('Scanning Probe Controller and Data Saver')
        self.show()

    def handleButton(self):
        '''This function allows me for getting the osilla to run'''
        self.lcd.display(self.osilla_run())

    def randomint(self):
        '''This is only test so I could update the PyQt display'''
        random = randint(2, 99)
        return random

    def osilla_run(self):
        '''This is accessing the modules I have build and updates the status bar'''
        from measurement_movement import func1
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        position = float(input('Enter the desired position of the stage'))
        func1(position)
        return position
    def zaber_run(self):
        '''This is accessing the modules I have build and updates the status bar'''
        from measurement_movement import func2
        func2()
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

def main():
    '''I do not need much to run it in main, just passed 10 to Scanning probe for some tests but never use anything, also I am handling here some errors'''
    app = QApplication(sys.argv)
    execute = Scanning_Probe(10)


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()