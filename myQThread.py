from PyQt5 import QtWidgets,QtCore

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        for i in range(1, 21):
            self.msleep(300)                   #сон на 3 сек
            # передачяа данных из потока через сигнал
            self.mysignal.emit(f'i = {i}')

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('для запуска потока нажать кнопку')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Запуск потока')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()      # экземпляр класса
        self.button.clicked.connect(self.on_clicked)
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)   # кнопка неактивна
        self.mythread.start()           # запуск потока

    def on_started(self):
        self.label.setText('Вызван метод on_started')
    
    def on_finished(self):
        self.label.setText('Вызван метод on_finished')
        self.button.setDisabled(False)  # кнопка активна

    def on_change(self, s):
        self.label.setText(s)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Использование класса QThread')
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
