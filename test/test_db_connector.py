from msqbitsReporter.database import db_connector

#if connection() return true then we've connected to the database
def test_connection():
    db = db_connector.DbConnector()
    assert db.connection() == True