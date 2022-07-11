
import sys
from zaber_motion import Library
# PREDEFINITIONS
Library.enable_device_db_store()

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Scanning_Probe(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Run the Osilla Measurement", self)
        btn1.setGeometry(100, 50, 200, 100)

        btn2 = QPushButton("Run the Zaber Movement", self)
        btn2.setGeometry(100, 250, 200, 100)

        btn1.clicked.connect(self.osilla_run)
        btn2.clicked.connect(self.zaber_run)

        self.statusBar()

        self.setGeometry(300, 300, 650, 550)
        self.setWindowTitle('Scanning Probe Controller and Data Saver')
        self.show()
    def osilla_run(self):
        from measurement_movement import func1
        func1()
    def zaber_run(self):
        from measurement_movement import func2
        func2()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


def main():
    app = QApplication(sys.argv)
    execute = Scanning_Probe()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()