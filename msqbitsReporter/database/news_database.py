import mysql.connector as mysql
from msqbitsReporter.database.db_connector import DbConnector
from msqbitsReporter.common import msqbitsReporterException


class News(DbConnector):
    def __init__(self):
        super().__init__()

    def insert_newspaper(self, name, website, feedlink, category):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO flux (nom_flux, adresse_flux, rss_flux, categorie_flux) "
                   "VALUES (%(nomFlux)s, %(adresseFlux)s, %(rssFlux)s, %(categorieFlux)s)")
        parameters = {'nomFlux': name, 'adresseFlux': website, 'rssFlux': feedlink, 'categorieFlux': category}

        try:
            cursor.execute(query, parameters)
            self.cnx.commit()
            return cursor.lastrowid

        except mysql.Error:
            raise msqbitsReporterException.InsertException

        finally:
            cursor.close()

    def select_newspaper_by_cat(self, name):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM flux f INNER JOIN categorie c ON c.id_categorie = f.categorie_flux WHERE " \
                "c.nom_categorie = %s "
        try:
            cursor.execute(query, (name,))
            return cursor.fetchall()

        except mysql.Error:
            raise msqbitsReporterException.FetchException

        finally:
            cursor.close()

    def select_newspaper_by_name(self, name):
        cursor = self.cnx.cursor(buffered=True)
        query = """SELECT * FROM flux f WHERE f.nom_flux = %s """

        try:
            cursor.execute(query, (name,))
            return cursor.fetchone()

        except mysql.Error:
            raise msqbitsReporterException.FetchException

        finally:
            cursor.close()

    def select_all_newspaper(self):
        cursor = self.cnx.cursor()
        query = "SELECT  f.nom_flux,  f.adresse_flux, c.nom_categorie,  f.rss_flux FROM flux f   INNER JOIN categorie " \
                "c ON c.id_categorie = f.categorie_flux "
        try:
            cursor.execute(query)
            return cursor.fetchall()

        except mysql.Error:
            raise msqbitsReporterException.FetchException

        finally:
            cursor.close()

    def select_categories(self):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM categorie"""

        try:
            cursor.execute(query)
            return cursor.fetchall()

        except mysql.Error:
            raise msqbitsReporterException.FetchException

        finally:
            cursor.close()

    def delete_newspaper(self, name):
        cursor = self.cnx.cursor()
        query = """DELETE FROM flux WHERE flux.nom_flux = %s """

        try:
            cursor.execute(query, (name,))
            self.cnx.commit()
            return True

        except mysql.Error:
            raise msqbitsReporterException.FetchException

        finally:
            cursor.close()
