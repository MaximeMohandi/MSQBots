import pytest
from msqbitsReporter import Database

def test_GetDatabaseCredentials():
    assert(Database.GetDatabaseCredentials()) == True
    pass

def test_ConnectToDatabase():
    pass

def test_DatabaseGetAllFlux():
    pass

def test_DatabaseGetAllCategorie():
    pass