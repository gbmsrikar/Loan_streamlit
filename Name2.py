import mysql.connector as mq

obj = mq.connect(user='root', password='12345',database='Practice', host='localhost', port=3306)

myc=obj.cursor()
myc.execute('CREATE DATABASE SQL_DB')
myc.close()
obj.close()


