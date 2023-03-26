from PyQt5 import QtWidgets, QtSql
import sys

# созлание объекта приложения - обязательно перед открытием базы данных, инча поддержка БД работать не будет
app = QtWidgets.QApplication(sys.argv)

# открытие базы данных в той же папке
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

query = QtSql.QSqlQuery()
query.prepare("\
    insert into good values(\
        null, :goodname, :goodcount)\
")

lst1 = ['Бумага', 'Карандаш', 'Картирдж', 'Линейка', 'Ручка']
lst2 = [250, 50, 2500, 100, 75]

query.bindValue(':goodname', lst1)
query.bindValue(':goodcount', lst2)

query.execBatch()


con.close()
