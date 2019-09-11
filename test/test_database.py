import pytest
import msqbitsReporter.Database as Database

def test_getDatabaseCredentials():
    db = Database.Database()
    credentials = db.getDataBaseCredentials()
    assert credentials.credentials['host'] != None

def test_connection():
    db = Database.Database()
    assert db.connection() == True

def test_getJournauxByCat():
    db = Database.Database()
    pass

def test_getJournalById():
    pass

def test_getJournalAll():
    pass

def test_getListCategory():
    pass

def test_updateJournal():
    pass

def removeJournal():
    pass