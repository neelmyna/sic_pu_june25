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

def creat_db():
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

connection = connect_db()
# connection.close() # to disconnect the DB
disconnect_db(connection)