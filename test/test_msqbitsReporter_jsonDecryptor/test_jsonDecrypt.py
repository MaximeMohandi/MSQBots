import pytest
from msqbitsReporter.msqbitsReporter_jsonDecryptor import jsonDecrypt, jsonDecryptorException

def test_ChargeJsonFile():
    falseJsonFile = open('ressources/test_falseJsonFile.txt').read()
    decrypt = jsonDecrypt.JsonDecrypt()
    with pytest.raises(jsonDecryptorException.NotJsonFormatException):
        decrypt.ChargeJsonFile(falseJsonFile)