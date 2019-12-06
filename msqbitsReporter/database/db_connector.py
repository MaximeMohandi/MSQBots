import mysql.connector as mysql
from msqbitsReporter.common import credentials

class DbConnector:
    def __init__(self):
        self.credentials = credentials.get_credentials('database')
        self.connection()

    def connection(self):
        try:
            self.cnx = mysql.connect(
                host=self.credentials['host'],
                port=self.credentials['port'],
                database=self.credentials['database'],
                user=self.credentials['user'],
                password=self.credentials['password']
            )
            return True
        except mysql.Error as error:
            raise error
