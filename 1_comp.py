from PyQt5 import QtWidgets
import sys, time

def on_clicked():
    button.setDisabled(True)                    #кнопка неактивна
    for i in range(1, 21):
        QtWidgets.qApp.processEvents()          #запуск оборота цикла
        time.sleep(1)                           #уснуть на 10 сек
        print('sleep -', i)
    button.setDisabled(False)                   #кнопка активна

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Запустить процесс')
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())
