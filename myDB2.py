from PyQt5 import QtWidgets, QtSql
import sys

# созлание объекта приложения - обязательно перед открытием базы данных, иначе поддержка БД работать не будет
app = QtWidgets.QApplication(sys.argv)

# открытие базы данных в той же папке
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('db_auto_order.sqlite')
con.open()

query = QtSql.QSqlQuery()
query.prepare("\
    insert into spec_region values(\
        null, :name)\
")

lst1 = [0, 1, 2, 3, 4]
lst2 = ['село', 'посёлок', 'пгт', 'город', 'зато']


query.bindValue(':id', lst1)
query.bindValue(':name', lst2)

query.execBatch()


con.close()
