from PyQt5 import QtWidgets, QtSql
import sys

# созлание объекта приложения - обязательно перед открытием базы данных, инча поддержка БД работать не будет
app = QtWidgets.QApplication(sys.argv)

# открытие базы данных в той же папке
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('db/db_auto_order.sqlite')
con.open()


# проверка наличия в базе данных таблицы spec_region, и, если такой нет, то создание такой
if 'spec_region' not in sorted(con.tables()):
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_region(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы region, и, если такой нет, то создание такой
if 'region' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table region(\
                id integer primary key autoincrement,\
                name text,\
                symbol text,\
                spec_region_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы spec_arial, и, если такой нет, то создание такой
if 'spec_arial' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_arial(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы arial, и, если такой нет, то создание такой
if 'arial' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table arial(\
                id integer primary key autoincrement,\
                name text,\
                spec_arial_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы spec_locality, и, если такой нет, то создание такой
if 'spec_locality' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_locality(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы locality, и, если такой нет, то создание такой
if 'locality' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table locality(\
                id integer primary key autoincrement,\
                name text,\
                spec_locality_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы area, и, если такой нет, то создание такой
if 'area' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table area(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")


# проверка наличия в базе данных таблицы spec_street, и, если такой нет, то создание такой
if 'spec_street' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_street(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы street, и, если такой нет, то создание такой
if 'street' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table street(\
                id integer primary key autoincrement,\
                name text,\
                spec_street_id integer\
               )\
    ")


# проверка наличия в базе данных таблицы spec_build, и, если такой нет, то создание такой
if 'spec_build' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_build(\
                id integer primary key autoincrement,\
                name text,\
                short_name text\
               )\
    ")

# проверка наличия в базе данных таблицы spec_room, и, если такой нет, то создание такой
if 'spec_room' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_room(\
                id integer primary key autoincrement,\
                name text,\
                short_name text\
               )\
    ")

# проверка наличия в базе данных таблицы bank, и, если такой нет, то создание такой
if 'bank' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table bank(\
                id integer primary key autoincrement,\
                name text,\
                BIK text,\
                INN text\
               )\
    ")

# проверка наличия в базе данных таблицы spec_job_title, и, если такой нет, то создание такой
if 'spec_job_title' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_job_title(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы executor, и, если такой нет, то создание такой
if 'executor' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table executor(\
                id integer primary key autoincrement,\
                name text,\
                short_name text,\
                INN text,\
                KPP text,\
                director_name text,\
                director_surname text,\
                director_otch text,\
                legal_address_build text,\
                legal_address_room text,\
                email text,\
                telephone text,\
                site text,\
                corr_check text,\
                bank_id integer,\
                acc_check text,\
                region_id text,\
                region_name text,\
                region_spec_region_id text,\
                arial_id text,\
                arial_spec_arial_id text,\
                locality_id text,\
                locality_spec_locality_id text,\
                area_id text,\
                street_id text,\
                street_spec_street_id text,\
                spec_build_id text,\
                spec_room_id text,\
                spec_job_title_id text\
               )\
    ")

# проверка наличия в базе данных таблицы customer, и, если такой нет, то создание такой
if 'customer' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table customer(\
                id integer primary key autoincrement,\
                name text,\
                short_name text,\
                INN text,\
                KPP text,\
                director_name text,\
                director_surname text,\
                director_otch text,\
                legal_address_build text,\
                legal_address_room text,\
                email text,\
                telephone text,\
                site text,\
                corr_check text,\
                bank_id integer,\
                acc_check text,\
                region_id text,\
                region_name text,\
                region_spec_region_id text,\
                arial_id text,\
                arial_spec_arial_id text,\
                locality_id text,\
                locality_spec_locality_id text,\
                area_id text,\
                street_id text,\
                street_spec_street_id text,\
                spec_build_id text,\
                spec_room_id text,\
                spec_job_title_id text\
               )\
    ")

# проверка наличия в базе данных таблицы spec_contract, и, если такой нет, то создание такой
if 'spec_contract' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_contract(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы contract, и, если такой нет, то создание такой
if 'contract' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table contract(\
                id integer primary key autoincrement,\
                number text,\
                date_of_conclusion date,\
                date_of_completion date,\
                summ double,\
                subject text,\
                short_subject text,\
                type text,\
                executor_id integer,\
                customer_id integer,\
                spec_contract_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы object, и, если такой нет, то создание такой
if 'object' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table object(\
                id integer primary key autoincrement,\
                name text,\
                region_id integer,\
                arial_id integer,\
                locality_id integer,\
                street_id integer,\
                area_id integer,\
                build_id integer,\
                number_build text,\
                room_id integer,\
                number_room integer,\
                period_of_maintence text,\
                contract_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы operation, и, если такой нет, то создание такой
if 'operation' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table operation(\
                id integer primary key autoincrement,\
                name text,\
                scope text,\
                regulations_id integer\
               )\
    ")

# проверка наличия в базе данных таблицы regulations, и, если такой нет, то создание такой
if 'regulations' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table regulations(\
                id integer primary key autoincrement,\
                name text,\
                period text\
               )\
    ")

# проверка наличия в базе данных таблицы spec_equipment, и, если такой нет, то создание такой
if 'spec_equipment' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table spec_equipment(\
                id integer primary key autoincrement,\
                name text\
               )\
    ")

# проверка наличия в базе данных таблицы equipment, и, если такой нет, то создание такой
if 'equipment' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("\
                create table equipment(\
                id integer primary key autoincrement,\
                name text,\
                spec_equipment_id integer,\
                operation_id integer,\
                object_id integer\
               )\
    ")


for table in con.tables():
    print(f'В таблице {table} {con.record(table).count()} поля(-ей)')

print(f'В БД всего {len(con.tables())} таблиц(-a,-ы)')

con.close()

