from PyQt5 import QtWidgets,QtCore

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False                    # флаг выолнения
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.mysignal.emit(f'count = {self.count}')
            self.sleep(1)

        # for i in range(1, 21):
        #     self.msleep(300)                   #сон на 3 сек
        #     # передачяа данных из потока через сигнал
        #     self.mysignal.emit(f'i = {i}')

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('для запуска потока нажать кнопку')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnStart = QtWidgets.QPushButton('Запуск потока')
        self.btnFinish = QtWidgets.QPushButton('Остановка процесса')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnFinish)
        self.setLayout(self.vbox)
        self.mythread = MyThread()      # экземпляр класса
        self.btnStart.clicked.connect(self.on_start)
        self.btnFinish.clicked.connect(self.on_finish)
        self.mythread.mysignal.connect(self.on_changed, QtCore.Qt.QueuedConnection)

        # self.mythread.started.connect(self.on_started)
        # self.mythread.finished.connect(self.on_finished)
        # self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()       # запуск потока

        # self.button.setDisabled(True)   # кнопка неактивна
        # self.mythread.start()           # запуск потока

    def on_finish(self):
        self.mythread.running = False     # изменение флага состояния

    def on_changed(self, s):
        self.label.setText(s)

    def closeEvent(self, event):           # фукция для закрытия окна
        self.hide()                         # скрыть окно
        self.mythread.running = False       # изменение флага выполнения
        self.mythread.wait(5000)            # время, чтобы закончить
        event.accept()                      # закрыть окно



    # def on_started(self):
    #     self.label.setText('Вызван метод on_started')
    
    # def on_finished(self):
    #     self.label.setText('Вызван метод on_finished')
    #     self.button.setDisabled(False)  # кнопка активна

    # def on_change(self, s):
    #     self.label.setText(s)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Запуск и остановка потока')
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
