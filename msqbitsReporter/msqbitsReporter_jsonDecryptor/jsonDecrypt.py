import json
from jsonDecryptorException import *

class JsonDecrypt :
    def __init__(self):
        self._jsonFile = None
    
    def ChargeJsonFile(self, file):
        self._jsonFile = file
        if self.FileIsJson() != True:
            raise NotJsonFormatException
        return None
    
    def FileIsJson(self):
        try:
            json.loads(self._jsonFile)
            return True
        except ValueError:
            return False
    
    def GetJsonObject(self):
        return None