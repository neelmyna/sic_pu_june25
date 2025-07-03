import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host='localhost', user="root", password="root123", datebase='nithin_db', port=3306, charset="utf8")
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB disconnection failed')

def create_db():
    query = 'create database IF NOT EXISTS nithin_db'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Database creation failed')

def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varcahr(50) not null, designation varchar(30), phone_number	bigint unique, salary float, commission		float default(0), years_of_experience tinyint, technology		varchar(30)	not null)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Table creation failed')


connection = connect_db()
# connection.close() # to disconnect the DB
disconnect_db(connection)