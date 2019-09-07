import pytest
from msqbitsReporter.msqbitsReporter_jsonDecryptor import jsonDecrypt


def test_ChargeJsonFile():
    falseJsonFile = open('ressources/test_falseJsonFile.txt').read()
    decrypt = jsonDecrypt.JsonDecrypt.ChargeJsonFile(falseJsonFile)