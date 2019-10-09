import mysql.connector as mysql
from msqbitsReporter.Database.db_connector import DbConnector
from msqbitsReporter.common import msqbitsReporterException

class News(DbConnector):
    def __init__(self):
        super().__init__()

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
        query = """SELECT 
                    f.nom_flux, 
                    f.adresse_flux,
                    c.nom_categorie, 
                    f.rss_flux
                FROM flux f 
                INNER JOIN categorie c ON c.id_categorie = f.categorie_flux"""
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