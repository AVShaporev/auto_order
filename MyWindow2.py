# -*- config: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
import time

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Нажмите кнопку, чтобы узнать текущее разрешение экрана')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Узнать разрешение')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.myrect)

    def myrect(self):
        desktop = QtWidgets.QApplication.desktop().screenGeometry()
        self.label.setText(f'Разрешение экрана на данный момент: {desktop.width()}*{desktop.height()}')
        self.button.setDisabled(True)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()                    # создание окна
    window.setWindowTitle('Заголовок окна')         # заголовок окна
    window.resize(300, 50)                          # размер окна



    window.show()




    sys.exit(app.exec_())
