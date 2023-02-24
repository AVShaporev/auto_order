from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
# print(QtWidgets.qApp.argv())
window = QtWidgets.QWidget()
window.setWindowTitle('FАвтоматизация отчетности ТО')
window.resize(300, 70)
label = QtWidgets.QLabel('<center>Фраза1</center>')
btnQuit = QtWidgets.QPushButton('&Закрыть')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
input()