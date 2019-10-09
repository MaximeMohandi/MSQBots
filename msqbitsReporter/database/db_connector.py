import mysql.connector as mysql
from msqbitsReporter.common import constant, JsonDecryptor, msqbitsReporterException

class DbConnector:
    def __init__(self):
        self.connection()

    def connection(self):
        try:
            self.getDataBaseCredentials()
            self.cnx = mysql.connect(
                host=self.credentials['host'],
                port=self.credentials['port'],
                database=self.credentials['database'],
                user=self.credentials['username'],
                password=self.credentials['password']
            )
            return True
        except mysql.Error:
            raise msqbitsReporterException.DatabaseException

    def getDataBaseCredentials(self):
        jsonData = JsonDecryptor.JsonDecryptor()
        credentialsPath = constant.DATABASE_CREDENTIALS_FILE
        try:
            jsonData.chargeJsonFile(credentialsPath)
            self.credentials = jsonData.getJsonObject()
        except msqbitsReporterException.JsonFormatFileException:
            return None