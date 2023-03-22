# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import MyWindow

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.MyWidget = MyWindow.MyWindow()
        self.MyWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton("&Check row")
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.MyWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)
    
    def on_clicked(self):
        self.MyWidget.label.setText(self.MyWidget.label.text() + '!')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('Преимущество ООП стиля')
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())