import mysql.connector  #pip install mysql-connector-python
from datetime import datetime
import psutil
def getusage():
    cpu = psutil.cpu_percent(0.1)
    ram = psutil.virtual_memory()[2]
    hdd = psutil.disk_usage('/')
    hdd = hdd.used / (2**30)

    # print(cpu)
    # print(ram)
    # print(hdd)
    return cpu , ram ,hdd
def db_creat():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="123",


    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS test1")

    mydb.close()
def db_table_creat():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        # auth_plugin='mysql_native_password',
        database="test1"
    )
    mycursor = mydb.cursor()
    rowcount =0
    mycursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES  WHERE table_name = 'dataa'")
    #mycursor.execute("SELECT * FROM testt1.TABLES")
    mycursor.fetchall()
    rowcount = mycursor.rowcount
    
    if rowcount==0:
        mycursor.execute("CREATE TABLE dataa ( time TEXT , cpu TEXT  , ram TEXT  , disk TEXT  ) ")

    mydb.close()
def insert_data():
    cpu , ram ,hdd = getusage()
    cpu = str(cpu)
    ram = str(ram)
    hdd = str(hdd)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        # auth_plugin='mysql_native_password',
        database="test1"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO dataa (time, cpu,ram,disk) VALUES (%s, %s,%s,%s)"
    val = (current_time, cpu,ram,hdd )
    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    #print(mycursor.rowcount, "record inserted.")
# print(mydb)

# Getting % usage of virtual_memory ( 3rd field)

db_creat()
db_table_creat()
insert_data()
