import pytest
import sys
from msqbitsReporter.msqbitsReporter_jsonDecryptor import jsonDecryptorException,jsonDecrypt

class TestJsoDecryptor:
    
    def test_ChargeJsonFile(self):
        falseJsonFile = open('test/test_msqbitsReporter_jsonDecryptor/ressources/test_falseJsonFile.txt','r')
        
        with pytest.raises(jsonDecryptorException.NotJsonFormatException):
            jsonDecryptor = jsonDecrypt.JsonDecrypt()
            jsonDecryptor.ChargeJsonFile(falseJsonFile)

    def test_GetJsonObject(self):
        pass