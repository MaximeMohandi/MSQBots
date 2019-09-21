import discord
from discord.ext import commands
from msqbitsReporter.common import constant, msqbitsReporterException, JsonDecryptor

def getCredentials():
    try:
        reader = JsonDecryptor.JsonDecryptor()
        reader.chargeJsonFile(constant.DISCORD_CREDENTIALS_FILE)
        return reader.getJsonObject()
    except msqbitsReporterException:
        print('erreur pendant la récupération des credentials')

credentials = getCredentials()
bot = commands.Bot(command_prefix=credentials['commandPrefix'])

def load_command_files():
    try:
        for file in constant.DISCORD_COMMANDS_FILES:
            bot.load_extension(file)
    except Exception as ex:
        print('error loading extension :')
        print(ex)

def run():
    try:
        load_command_files()
        bot.run(credentials['token'], bot=True, reconnect=True)
    except Exception as ex:
        print('erreur lors du démarrage :')
        print(ex)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=credentials['messageActivity']))
    print("I'm on the case")

@bot.event
async def on_error(event, *args, **kwargs):
    print('une erreur est survenue')

@bot.event
async def on_disconnect():
    print('Free time !!')