from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Атоматизация отчетности')
window.resize(500, 70)
label = QtWidgets.QLabel('<center>Привет, мир!</center>')
btnQuit = QtWidgets.QPushButton('&Закрыть')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())