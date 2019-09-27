import json
import os.path as path

respath = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'msqbitsReporter/ressources/')

def ask_database_credentials():
    checked = False
    displayerror = False
    titlemessage = '------configuration database--------'

    while checked == False:
        if displayerror != checked:
            titlemessage = '[ERROR] information is missing '

        print(titlemessage)
        dbhost = input('host: ')
        dbport = input('port: ')
        dbname = input('name: ')
        dbuser = input('user: ')
        dbpwd = input('password: ')

        checked = check_mandatory_field(
            {dbhost, dbport, dbname, dbuser, dbpwd}
        )

    dbwriter = open(respath + 'databaseParameter.json', 'w+')
    dbwriter.write(json.dumps(
        {
            "host": dbhost,
            "port": dbport,
            "database": dbname,
            "username": dbuser,
            "password": dbpwd
        }
    ))

def ask_discord_credentials():
    checked = False
    displayerror = False
    titlemessage = '------configuration discord name---------'

    while checked == False:
        if displayerror != checked:
            titlemessage = '[ERROR] information is missing '

        print(titlemessage)
        bottoken = input('bot token: ')
        botchannel = input('bot default channel id: ')
        botmessage = input('bot activity message: ')
        botprefix = input('bot prefix : ')

        checked = check_mandatory_field(
            {bottoken, botchannel, botmessage, botprefix}
        )

    discordwriter = open(respath + 'discordsCredentials.json', 'w+')
    discordwriter.write(json.dumps(
        {
            "token": bottoken,
            "channelId": botchannel,
            "messageActivity": botmessage,
            "commandPrefix": botprefix,
        }
    ))

def check_mandatory_field(tocheck):
    if '' in tocheck:
        return False
    else:
        return True


ask_database_credentials()
ask_discord_credentials()

