import pytest
import msqbitsReporter.Database as Database

#if the host is not null then we correctly get the credentials
def test_getDatabaseCredentials():
    db = Database.Database()
    credentials = db.getDataBaseCredentials()
    assert db.credentials['host'] != None

#if connection() return true then we've connected to the database
def test_connection():
    db = Database.Database()
    assert db.connection() == True

#if result is superio to 0 then we've get the last id inserted
def test_insertJournal():
    db = Database.Database()
    result = db.insertJournal(
        'test_insertJournal',
        'test_insertJournal',
        'test_insertJournal',
        5
    )
    assert result > 0
    db.cnx.rollback()

def test_getJournauxByCat():
    db = Database.Database()
    result = db.getJournauxByCat(5) #here 5 is the index for the test cat
    assert len(result) > 0

def test_getJournalById():
    db = Database.Database()
    testRow = db.getJournauxByCat(5) #we get a list of test row to select one row
    testRowFluxId = testRow[0].id_flux #TODO get the correct value to pass at getJournalByID
    result = db.getJournalById(testRowFluxId)
    assert result > 0


def test_getJournalAll():
    pass

def test_getListCategory():
    pass

def test_updateJournal():
    pass

def test_removeJournal():
    pass