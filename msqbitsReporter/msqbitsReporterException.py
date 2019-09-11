class msqbitsReporterException(Exception):
    pass

class JsonFormatFileException(msqbitsReporterException):
    """The File is not a Json File, please charge a json file"""
    pass

class DatabaseException(msqbitsReporterException):
    """A problem occured with the database"""
    pass

class InsertException(DatabaseException):
    """A problem occured with the insertion into the database"""
    pass

class FetchException(DatabaseException):
    """A problem occured with the select command"""
    pass