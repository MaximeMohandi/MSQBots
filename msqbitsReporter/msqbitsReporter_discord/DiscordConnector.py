import os
import discord
from discord.ext import commands
from msqbitsReporter.msqbitsReporterException import msqbitsReporterException
import msqbitsReporter.JsonDecryptor as JsonDecryptor

def getCredentials():
    try:
        credentialsPath = os.path.join(os.path.dirname(__file__), 'ressources/discordsCredentials.json')
        reader = JsonDecryptor.JsonDecryptor()
        reader.chargeJsonFile(credentialsPath)
        return reader.getJsonObject()
    except msqbitsReporterException:
        print('erreur pendant la récupération des credentials')

credentials = getCredentials()
bot = commands.Bot(command_prefix=credentials['commandPrefix'])

def run():
    try:
        bot.run(credentials['token'])
    except Exception:
        print('erreur')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=credentials['messageActivity']))
    print("I'm on the case")


@bot.event
async def on_error(event, *args, **kwargs):
    print('une erreur est survenue')
