from PyQt5 import QtWidgets, QtSql
import sys

# созлание объекта приложения - обязательно перед открытием базы данных, инча поддержка БД работать не будет
app = QtWidgets.QApplication(sys.argv)

# открытие базы данных в той же папке
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

query = QtSql.QSqlQuery()
query.exec("select * from good order by goodname")
lst =[]

if query.isActive():
    query.first()
    while query.isValid():
        lst.append(str(query.value('goodname')) + '-' + str(query.value('goodcount')))
        query.next()
    
    for p in lst: print(p)

con.close()
 