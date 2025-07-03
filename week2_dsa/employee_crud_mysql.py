import pymysql

def connectDb():
    connection = None
    try:
        connection = pymysql.Connect(host="localhost", user="root", password="root123", datebase="nithin_db", port=3306, charset="utf-8")
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

connection = connectDb()