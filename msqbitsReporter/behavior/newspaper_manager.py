from msqbitsReporter.common import Database
import feedparser

db = Database.Database()

def addNewsPaper(newNewspaper) :
    db.insertJournal(
        newNewspaper['nom_flux'],
        newNewspaper['adresse_flux'],
        newNewspaper['rss_flux'],
        newNewspaper['categorie_flux']
    )

def removeNewsPaper(newsPaperToRemove) :
    db.removeJournal(newsPaperToRemove)
