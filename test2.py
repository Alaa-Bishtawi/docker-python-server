import mysql.connector  #pip install mysql-connector-python

def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="test1"

    )

    return mydb.cursor(),mydb

def cpu_retrive():
    rowcount = 0


    mycursor,mydb = connect_db()
    mycursor.execute("SELECT time,cpu FROM dataa")

    myresult = mycursor.fetchall()
    rowcount = mycursor.rowcount
    strr = ''
    j =0
    for x in myresult:
        if j<24 :
            strr = strr +  " Time : " + x[0] + " cpu usage : " + x[1] + "\n"
            j = j+1
        else:

            break

    #print(strr)
    mydb.close()
    return strr


def ram_retrive():
    rowcount = 0


    mycursor, mydb = connect_db()
    mycursor.execute("SELECT time,ram FROM dataa")

    myresult = mycursor.fetchall()
    rowcount = mycursor.rowcount
    strr = ''
    j = 0
    for x in myresult:
        if j < 24:
            strr = strr + " Time : " + x[0] + " ram usage : " + x[1] + "\n"
            j = j + 1
        else:

            break

    #print(strr)
    mydb.close()
    return strr
def hdd_retrive():
    rowcount = 0


    mycursor , mydb = connect_db()
    mycursor.execute("SELECT time,disk FROM dataa")

    myresult = mycursor.fetchall()
    rowcount = mycursor.rowcount
    strr = ''
    j = 0
    for x in myresult:
        if j < 24:
            strr = strr + " Time : " + x[0] + " disk usage : " + x[1] + "\n"
            j = j + 1
        else:

            break

    print(strr)
    mydb.close()
    return strr

