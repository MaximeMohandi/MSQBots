from msqbitsReporter.database import news_database


#if result is superio to 0 then we've get the last id inserted
def test_insertJournal():
    db = news_database.News()
    result = db.insert_newspaper(
        'test_insertJournal',
        'test_insertJournal',
        'test_insertJournal',
        5
    )
    assert result > 0
    db.cnx.rollback()


def test_getJournauxByCat():
    db = news_database.News()
    result = db.select_newspaper_by_cat('TEST') #here 5 is the index for the test cat
    assert len(result) > 0


def test_getJournalByNom():
    db = news_database.News()
    testRows = db.select_newspaper_by_cat('TEST') #we get a list of test row to select one row
    testFirstRow = testRows[0]
    nomFirstRow = testFirstRow[1]
    result = db.select_newspaper_by_name(nomFirstRow)
    assert len(result) > 0


def test_getJournalAll():
    db = news_database.News()
    result = db.select_all_newspaper()
    assert len(result) > 0


def test_getListCategory():
    db = news_database.News()
    result = db.select_categories()
    assert len(result) > 0


def test_updateJournal():
    pass

def test_removeJournal():
    db = news_database.News()
    toRemoveJournalList = db.select_newspaper_by_cat('TEST') #get all journal from test category
    toRemoveJournal = toRemoveJournalList[0] #get the first journal from the test journal list
    idJournalToRemove = toRemoveJournal[0]
    assert db.delete_newspaper(idJournalToRemove) == True
