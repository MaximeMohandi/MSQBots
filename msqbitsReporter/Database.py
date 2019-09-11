import mysql.connector as mysql
import msqbitsReporter.JsonDecryptor as JsonDecryptor
import msqbitsReporter.msqbitsReporterException as error

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
            raise error.DatabaseException
        
    def getDataBaseCredentials(self):
        jsonData = JsonDecryptor.JsonDecryptor()
        credentialsPath = 'msqbitsReporter/ressources/databaseParameter.json'
        try :
            jsonData.chargeJsonFile(credentialsPath)
            self.credentials = jsonData.getJsonObject()
        except error.JsonFormatFileException:
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
            raise error.InsertException
        finally:
            cursor.close()

    def getJournauxByCat(self, catId):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM flux WHERE categorie_flux = %s """

        try:
            cursor.execute(query, (catId,))
            return cursor.fetchall()
        except mysql.Error:
            raise error.FetchException
        finally:
            cursor.close()

    def getJournalById(self, journalID):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM flux WHERE id_flux = %s """

        try:
            cursor.execute(query, journalID)
            return cursor.fetchall()
        except mysql.Error:
            raise error.FetchException
        finally:
            cursor.close()

    def getJournalAll(self):
        #requete pour récupérer tous les journaux 
        pass
    
    def getListCategory(self):
        #requete retourne toutes les catégories
        pass

    def updateJournal(self, journalObject):
        #update un journal
        pass

    def removeJournal(self, journalID):
        pass