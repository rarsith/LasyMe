# importing libraries
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating progress bar
        bar = QProgressBar(self)

        # setting geometry to progress bar
        bar.setGeometry(200, 150, 40, 200)

        # set value to progress bar
        bar.setValue(70)

        # changing the orientation
        bar.setOrientation(QtCore.Qt.Vertical)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())