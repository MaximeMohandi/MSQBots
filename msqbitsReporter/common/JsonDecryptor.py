import json
import msqbitsReporter.common.msqbitsReporterException as error

class JsonDecryptor:
    def __init__(self):
        pass

    def chargeJsonFile(self, file):
        try:
            with open(file) as jsonData:
                self._jsonFile = json.load(jsonData)
        except (ValueError, TypeError):
            raise error.JsonFormatFileException

    def getJsonObject(self):
        return self._jsonFile
