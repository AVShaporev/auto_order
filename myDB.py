from PyQt5 import QtWidgets, QtSql
import sys

# созлание объекта приложения - обязательно перед открытием базы данных, инча поддержка БД работать не будет
app = QtWidgets.QApplication(sys.argv)

# открытие базы данных в той же папке
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

# провекра наличия в базе данных таблицы good, и, если такой нет, то создание такой
if 'good' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
        create table good(\
            id integer primary key autoincrement,\
            goodname text,\
            goodcount integer)\
    ")

con.close()

