import json
import jsonDecryptorException

_jsonFile = None

def ChargeJsonFile(file):
    _jsonFile = file
    if FileIsJson() != True:
        raise jsonDecryptorException.NotJsonFormatException
    else:
        #TODO creer objet a partir du JSON
        pass
    
def FileIsJson():
    try:
        json.loads(_jsonFile)
        return True
    except ValueError:
        return False

def GetJsonObject():
    return None