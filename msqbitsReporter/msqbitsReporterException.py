class msqbitsReporterException(Exception):
    pass

class JsonFormatFileException(msqbitsReporterException):
    """The File is not a Json File, please charge a json file"""
    pass
