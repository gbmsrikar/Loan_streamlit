import mysql.connector as mq
obj = mq.connect(user='root', password='12345',database='Practice', host='localhost', port=3306)

s='CREATE TABLE table1(empid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),id INT,salary FLOAT)'
myc=obj.cursor()
myc.execute(s)
myc.close()
obj.close()


