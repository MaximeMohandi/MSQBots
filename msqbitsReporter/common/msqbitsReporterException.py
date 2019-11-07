class msqbitsReporterException(Exception):
    pass

class DatabaseException(msqbitsReporterException):
    def __init__(self):
        self.message = 'A problem occured with the database'


class InsertException(DatabaseException):
    def __init__(self):
        self.message = 'A problem occured with the insertion into the database'


class FetchException(DatabaseException):
    def __init__(self):
        self.message = 'A problem occured when fetching data'
