import pytest
from msqbitsReporter import msqbitsReporterException
from msqbitsReporter.JsonDecryptor import JsonDecryptor

def test_ChargeJsonFile():
    fakeFilePath = "/ressources/test_fakeJsonFile.txt"
    decryptor = JsonDecryptor.JsonDecryptor()
    with pytest.raises(msqbitsReporterException.JsonFormatFileException):
        decryptor.ChargeJsonFile(fakeFilePath)