from msqbitsReporter.Database import news_database


#if the host is not null then we correctly get the credentials
def test_getDatabaseCredentials():
    db = news_database.News()
    credentials = db.getDataBaseCredentials()
    assert db.credentials['host'] != None

#if connection() return true then we've connected to the database
def test_connection():
    db = news_database.News()
    assert db.connection() == True

#if result is superio to 0 then we've get the last id inserted
def test_insertJournal():
    db = news_database.News()
    result = db.insertJournal(
        'test_insertJournal',
        'test_insertJournal',
        'test_insertJournal',
        5
    )
    assert result > 0
    db.cnx.rollback()

def test_getJournauxByCat():
    db = news_database.News()
    result = db.getJournauxByCat('TEST') #here 5 is the index for the test cat
    assert len(result) > 0

def test_getJournalByNom():
    db = news_database.News()
    testRows = db.getJournauxByCat('TEST') #we get a list of test row to select one row
    testFirstRow = testRows[0]
    nomFirstRow = testFirstRow[1]
    result = db.getJournalByNom(nomFirstRow)
    assert len(result) > 0

def test_getJournalAll():
    db = news_database.News()
    result = db.getJournalAll()
    assert len(result) > 0

def test_getListCategory():
    db = news_database.News()
    result = db.getListCategory()
    assert len(result) > 0

def test_updateJournal():
    pass

def test_removeJournal():
    db = news_database.News()
    toRemoveJournalList = db.getJournauxByCat('TEST') #get all journal from test category
    toRemoveJournal = toRemoveJournalList[0] #get the first journal from the test journal list
    idJournalToRemove = toRemoveJournal[0]
    assert db.removeJournal(idJournalToRemove) == True     