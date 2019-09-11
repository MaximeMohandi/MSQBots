import pytest
import msqbitsReporter.msqbitsReporterException as msqbitsReporterException
import msqbitsReporter.JsonDecryptor as JsonDecryptor

def test_ChargeJsonFile():
    fakeFilePath = getFakeJsonFile()
    decryptor = JsonDecryptor.JsonDecryptor()
    with pytest.raises(msqbitsReporterException.JsonFormatFileException):
        decryptor.chargeJsonFile(fakeFilePath)

def test_getJsonObject():
    decryptor = JsonDecryptor.JsonDecryptor()
    decryptor.chargeJsonFile(getTrueJsonFile())
    returnedJson = decryptor.getJsonObject()
    assert returnedJson['test'] == True

def getFakeJsonFile():
    return 'test/ressources/test_fakeJsonFile.txt'

def getTrueJsonFile():
    return 'test/ressources/test_TrueJsonFile.json'