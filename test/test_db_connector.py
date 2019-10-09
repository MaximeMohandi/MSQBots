from msqbitsReporter.database import db_connector

#if the host is not null then we correctly get the credentials
def test_getDatabaseCredentials():
    db = db_connector.DbConnector()
    credentials = db.getDataBaseCredentials()
    assert db.credentials['host'] != None

#if connection() return true then we've connected to the database
def test_connection():
    db = db_connector.DbConnector()
    assert db.connection() == True