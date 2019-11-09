import configparser
import os.path as path

path = path.join(path.dirname(path.dirname(path.abspath(__file__))), '../msqbitsReporter/resources/config.ini')
config = configparser.ConfigParser()


print("+-----------------------+")
print("|     Config Writer     |")
print("+-----------------------+\n")


def check_mandatory_fields(fields):
    if '' in fields:
        return False
    else:
        return True


def write_db_config():
    dbhost = ''
    dbport = ''
    dbname = ''
    dbuser = ''
    dbpwd = ''

    while not check_mandatory_fields({dbhost, dbport, dbname, dbuser, dbpwd}):
        print('-----------DATABASE-------------')
        dbhost = input('host: ')
        dbport = input('port: ')
        dbname = input('database: ')
        dbuser = input('user: ')
        dbpwd = input('password: ')

    config['DATABASE'] = {
        'host': dbhost,
        'port': dbport,
        'database': dbname,
        'user': dbuser,
        'password': dbpwd
    }


def write_discord_config():
    token = ''
    messageActivity = ''
    commandPrefix = ''

    while not check_mandatory_fields({token, messageActivity, commandPrefix}):
        print('---------------------DISCORD------------')
        token = input('bot token: ')
        messageActivity = input('message activity: ')
        commandPrefix = input('command prefix: ')

    config['DISCORD'] = {
        'token': token,
        'messageActivity': messageActivity,
        'commandPrefix': commandPrefix
    }


write_db_config()
write_discord_config()
with open(path, 'w+') as configfile:
    config.write(configfile)
