import mysql.connector

class Database:
    def __init__(self):
        pass
    
    def connection():
        #todo récuperer ls données depuis le fichier de credentials
        pass

    def GetDataBaseCredentials(self):
        pass

    def GetJournauxByCat(self, catId):
        #todo requete pour récuperer les journanux 
        # par catégories et les renvoyer sous forme de list d'objet
        pass

    def GetJournalById(self, journalID):
        #todo requete pour récupérer un journal et renvoyé une liste de tous ses articles
        pass

    def GetJournalAll(self):
        #requete pour récupérer tous les journaux 
        pass
    
    def GetListCategory(self):
        #requete retourne toutes les catégories
        pass

    def UpdateJournal(self, journalObject):
        #update un journal
        pass

    def RemoveJournal(self, journalID):
        pass