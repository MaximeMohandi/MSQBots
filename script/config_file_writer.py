import configparser
# import os.path as path

path = 'msqbot/resources/config.ini'
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
    message_activity = ''
    command_prefix = ''
    edt_channel = ''
    meter_channel = ''

    while not check_mandatory_fields({token, message_activity, command_prefix}):
        print('---------------------DISCORD------------')
        token = input('bot token: ')
        message_activity = input('message activity: ')
        command_prefix = input('command prefix: ')
        edt_channel = input('id channel for planning: ')
        meter_channel = input('id channel for meters: ')

    config['DISCORD'] = {
        'token': token,
        'message_activity': message_activity,
        'command_prefix': command_prefix,
        'idEdtChannel': edt_channel,
        'idMeterChannel': meter_channel
    }


write_discord_config()
with open(path, 'w+') as configfile:
    config.write(configfile)
