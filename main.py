import os.path
import sys
from zaber_motion import Library
import matplotlib
# PREDEFINITIONS REQUIRED FOR STAGES
Library.enable_device_db_store()
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QLineEdit,QVBoxLayout, QApplication, QMessageBox, QLabel)
from PyQt5.QtCore import QTime, QTimer
###TEST ONLY
from random import randint
###TEST ONLY
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=50, height=40, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Scanning_Probe(QMainWindow):
    '''Here I am describbing how my window is being made and how all classes are built'''
    def __init__(self, position):
        super().__init__()
        self.position = 0
        self.initUI()

    def initUI(self):
        '''Here I initialise all window and display'''
        # sc = MplCanvas(self, width=50, height=40, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # sc.setFixedSize(300,300)
        #
        # #self.setCentralWidget(sc)

        self.lcd = QLCDNumber(self)
        self.file = QLCDNumber(self)
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        self.lcd.setGeometry(300, 150, 250, 150)
        layout.addWidget(self.file)
        self.file.setGeometry(300, 450, 250, 150)
        self.setLayout(layout)
        self.check_if_file_exist()

        btn1 = QPushButton("Measure to file", self)
        btn1.setGeometry(100, 150, 200, 150)
        self.btn2 = QPushButton("Online measurement!", self)
        self.btn2.setEnabled(False)
        self.btn2.setGeometry(100, 300, 200, 150)
        btn3 = QPushButton("Emergency stop button!!!", self)
        btn3.setGeometry(100, 450, 200, 150)
        btn1.clicked.connect(self.osilla_run)
        self.btn2.clicked.connect(self.zaber_run)
        btn3.clicked.connect(self.handleButton)
        #lcd.display(self.osilla_run())
        # Create textbox
        self.speed_input = QLineEdit(self)
        self.speed_input.move(100, 5)
        self.speed_input.resize(280, 40)

        self.position_input = QLineEdit(self)
        self.position_input.move(100, 45)
        self.position_input.resize(280, 40)

        # Create a button in the window
        self.speed_button = QPushButton('Set speed', self)
        self.speed_button.move(420, 5)
        self.position_button = QPushButton('Set position', self)
        self.position_button.move(420, 45)
        self.position_current()

        # connect button to function on_click
        self.speed_button.clicked.connect(self.on_click)
        self.position_button.clicked.connect(self.position_setter)

        self.statusBar()
        self.setGeometry(300, 300, 950, 850)
        self.setWindowTitle('Scanning Probe Controller and Data Saver')
        self.show()
#HERE I DEMONSTRATE HOW TO USE DECORATOR
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.speed_input.text()
        QMessageBox.question(self, 'FOR SAFETY HOMING OF THE STAGE WILL BE PERFORMED', "Your speed is: " + textboxValue + "mm/s", QMessageBox.Ok, QMessageBox.Ok)
        self.speed_input.setText("")
        from measurement_movement import func_speed
        func_speed(int(textboxValue))
        self.position_current()
        #self.position_button.setText("")


    @pyqtSlot()
    def position_setter(self):
        from measurement_movement import func_position
        textboxValue = self.position_input.text()
        if int(textboxValue)>=400:
            self.btn2.setEnabled(True)

        QMessageBox.question(self, 'You have set the position', "Your position is: " + textboxValue + "mm", QMessageBox.Ok, QMessageBox.Ok)

        from measurement_movement import func_position
        func_position(int(textboxValue))
        position_verifier = int(textboxValue)
        self.position_current()
        return position_verifier

        #self.position_button.setText("")

    def handleButton(self):
        '''This function allows me for getting the osilla to run'''
        sys.exit()

    def randomint(self):
        '''This is only test so I could update the PyQt display'''
        random = randint(2, 99)
        return random

    def check_if_file_exist(self):

        if os.path.exists('measurement.csv') == True:
            self.file.display(1)
        else:
            self.file.display(0)

    def position_current(self):
        from measurement_movement import temperature
        self.lcd.display(temperature())

    def osilla_run(self):
        '''This is accessing the modules I have build and updates the status bar'''
        from file_saving import main as current_measure
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        current_measure()
    def zaber_run(self):
        '''This is accessing the modules I have build and updates the status bar'''
        from file_displaying_online import visual as vis
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        vis()
        self.position_current()

def main():
    '''I do not need much to run it in main, just passed 10 to Scanning probe for some tests but never use anything, also I am handling here some errors'''
    app = QApplication(sys.argv)
    execute = Scanning_Probe(10)


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()