class JsonDecryptorException(Exception):
    pass

class NotJsonFormatException(Exception):
    def __init__(self):
        self.message = 'the file is not in json format'