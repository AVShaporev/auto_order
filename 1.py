from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Phrase1")
        self.label.setAlignment(QtCore.Qt)

print('Работа приложения завершена!')
