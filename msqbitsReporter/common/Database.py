import mysql.connector as mysql
from msqbitsReporter.common import constant, JsonDecryptor, msqbitsReporterException

class Database:
    def __init__(self):
        self.connection()
    
    def connection(self):
        try:
            self.getDataBaseCredentials()
            self.cnx = mysql.connect(
                host = self.credentials['host'],
                port = self.credentials['port'],
                database = self.credentials['database'],
                user = self.credentials['username'],
                password = self.credentials['password']
            )
            return True
        except mysql.Error:
            raise msqbitsReporterException.DatabaseException
        
    def getDataBaseCredentials(self):
        jsonData = JsonDecryptor.JsonDecryptor()
        credentialsPath = constant.DATABASE_CREDENTIALS_FILE
        try :
            jsonData.chargeJsonFile(credentialsPath)
            self.credentials = jsonData.getJsonObject()
        except msqbitsReporterException.JsonFormatFileException:
            return None

    def insertJournal(self, nomFlux, adresseFlux, rssFlux, categorieFlux):
        cursor = self.cnx.cursor()
        addFlux = ("INSERT INTO flux "
                "(nom_flux, adresse_flux, rss_flux, categorie_flux)" 
                "VALUES (%(nomFlux)s, %(adresseFlux)s, %(rssFlux)s, %(categorieFlux)s)")
        dataFlux = {
            'nomFlux': nomFlux,
            'adresseFlux': adresseFlux,
            'rssFlux': rssFlux,
            'categorieFlux': categorieFlux,
        }
        
        try: 
            cursor.execute(addFlux, dataFlux)
            self.cnx.commit()
            return cursor.lastrowid
        except mysql.Error:
            raise msqbitsReporterException.InsertException
        finally:
            cursor.close()

    def getJournauxByCat(self, catNom):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM flux f
                INNER JOIN categorie c ON c.id_categorie = f.categorie_flux
                WHERE c.nom_categorie = %s """

        try:
            cursor.execute(query, (catNom,))
            return cursor.fetchall()
        except mysql.Error:
            raise msqbitsReporterException.FetchException
        finally:
            cursor.close()

    def getJournalByNom(self, nomJournal):
        cursor = self.cnx.cursor(buffered=True)
        query = """SELECT * FROM flux f
                WHERE f.nom_flux = %s """

        try:
            cursor.execute(query, (nomJournal,))
            return cursor.fetchone()
        except mysql.Error:
            raise msqbitsReporterException.FetchException
        finally:
            cursor.close()

    def getJournalAll(self):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM flux"""

        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.Error:
            raise msqbitsReporterException.FetchException
        finally:
            cursor.close() 
    
    def getListCategory(self):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM categorie"""

        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.Error:
            raise msqbitsReporterException.FetchException
        finally:
            cursor.close() 

    def updateJournal(self, journalObject):
        #update un journal
        pass

    def removeJournal(self, nomJournal):
        cursor = self.cnx.cursor()
        query = """DELETE FROM flux WHERE flux.nom_flux = %s """

        try:
            cursor.execute(query, (nomJournal,))
            self.cnx.commit()
            return True
        except mysql.Error:
            raise msqbitsReporterException.FetchException
        finally:
            cursor.close()