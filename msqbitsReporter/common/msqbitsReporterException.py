class msqbitsReporterException(Exception):
    pass


class JsonFormatFileException(msqbitsReporterException):
    def __init__(self):
        self.message = 'The File is not a Json File, please charge a json file'


class DatabaseException(msqbitsReporterException):
    def __init__(self):
        self.message = 'A problem occured with the database'


class InsertException(DatabaseException):
    def __init__(self):
        self.message = 'A problem occured with the insertion into the database'


class FetchException(DatabaseException):
    def __init__(self):
        self.message = 'A problem occured when fetching data'
