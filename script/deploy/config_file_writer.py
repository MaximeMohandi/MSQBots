import configparser
import os.path as path

path = path.join(path.dirname(path.dirname(path.abspath(__file__))), '../msqbot/resources/config.ini')
config = configparser.ConfigParser()


print("+-----------------------+")
print("|     Config Writer     |")
print("+-----------------------+\n")


def check_mandatory_fields(fields):
    if '' in fields:
        return False
    else:
        return True


def write_discord_config():
    token = ''
    messageActivity = ''
    commandPrefix = ''
    news_channel = ''
    edt_channel = ''

    while not check_mandatory_fields({token, messageActivity, commandPrefix}):
        print('---------------------DISCORD------------')
        token = input('bot token: ')
        messageActivity = input('message activity: ')
        commandPrefix = input('command prefix: ')
        news_channel = input('id channel for news: ')
        edt_channel = input('id channel for planning: ')

    config['DISCORD'] = {
        'token': token,
        'messageActivity': messageActivity,
        'commandPrefix': commandPrefix,
        'idNewsChannel': news_channel,
        'idEdtChannel': edt_channel
    }


write_discord_config()
with open(path, 'w+') as configfile:
    config.write(configfile)
