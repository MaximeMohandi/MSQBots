import json
import sys
from .jsonDecryptorException import NotJsonFormatException

class JsonDecrypt:
    def __init__(self):
        self._jsonFile = None
        self._jsonObject = None

    def ChargeJsonFile(self,file):
        print(file)
        self._jsonFile = file
        
        if self.FileIsJson():
            with open(self._jsonFile,'r') as read_file:
                self._jsonObject = read_file
        else:
            raise NotJsonFormatException
        
    def FileIsJson(self):
        try:
            json.loads(self._jsonFile)
            return True
        except (TypeError, ValueError):
            return False

    def GetJsonObject(self):
        return self._jsonObject