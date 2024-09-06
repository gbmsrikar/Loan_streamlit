import mysql as mq
import mysql.connector as mq
try:
    obj=mq.connect(user='root',password='12345',host='localhost',port=3306)
    if obj.is_connected():
        print('Connected')
except:
    print('unable to connect')
s='SHOW DATABASES'
myc=obj.cursor()
myc.execute(s)
for d in myc:
    print(d)
myc.close()
obj.close()



