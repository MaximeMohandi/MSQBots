import msqbitsReporter.common.credentials as credentials

def test_get_credentials():
    credentials.get_credentials('discord') != None