import mysql.connector
import msqbitsReporter.JsonDecryptor as JsonDecryptor
import msqbitsReporter.msqbitsReporterException as error

class Database:
    def __init__(self):
        pass
    
    def connection(self):
        #todo récuperer ls données depuis le fichier de credentials
        pass

    def getDataBaseCredentials(self):
        jsonData = JsonDecryptor.JsonDecryptor()
        credentialsPath = 'msqbitsReporter/ressources/databaseParameter.json'
        try :
            jsonData.chargeJsonFile(credentialsPath)
            self.credentials = jsonData.getJsonObject()
        except error.JsonFormatFileException:
            return None

    def getJournauxByCat(self, catId):
        #todo requete pour récuperer les journanux 
        # par catégories et les renvoyer sous forme de list d'objet
        pass

    def getJournalById(self, journalID):
        #todo requete pour récupérer un journal et renvoyé une liste de tous ses articles
        pass

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