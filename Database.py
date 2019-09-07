import mysql.connector

host = "db5000120702.hosting-data.io"
usr = "dbu216484"
pwd = "2$4fbc%S_5"

class Database:
    mydb = None
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host,
            usr,
            pwd
        )

    def GetCat():
        global mydb
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM categorie")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

