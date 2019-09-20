import pytest
import os
import msqbitsReporter.common.msqbitsReporterException as msqbitsReporterException
import msqbitsReporter.common.JsonDecryptor as JsonDecryptor

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
    return os.path.join(os.path.dirname(__file__), 'ressources/test_fakeJsonFile.txt')

def getTrueJsonFile():
    return os.path.join(os.path.dirname(__file__), 'ressources/test_TrueJsonFile.json')