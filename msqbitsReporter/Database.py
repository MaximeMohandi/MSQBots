import mysql.connector

class Database:
    def __init__(self):
        pass
    
    def connection():
        #todo récuperer ls données depuis le fichier de credentials
        pass

    def getDataBaseCredentials(self):
        pass

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