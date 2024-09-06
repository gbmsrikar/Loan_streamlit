from mysql.connector import connect
import streamlit as st
try:
    obj=connect(user='root',password='12345',database='sql_db',host='localhost',port=3306)
    if (obj.is_connected()):
        print('Connected')
except:
    print('unable to connect')
myc=obj.cursor()
myc.execute('select * from table3')
data=myc.fetchall()
for i in data:
    print(i)
import pandas as pd
st.title('MySQL Dataset')
df=pd.DataFrame(data)
st.write(df)

def main():
    st.title("Operations With MySQL");
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        age=st.number_input("Enter age")
        if st.button("Create"):
            sql= "insert into table3(name,age) values(%s,%s)"
            val= (name,age)
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Created Successfully!!!")
if _name_ == "_main_":
main()

