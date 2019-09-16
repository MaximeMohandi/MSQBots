import asyncio
import discord
from discord.ext import commands
from msqbitsReporter.msqbitsReporterException import msqbitsReporterException
from msqbitsReporter.msqbitsReporter_discord import CommandReaction
import msqbitsReporter.JsonDecryptor as JsonDecryptor

credentials = getCredentials()
bot = commands.Bot(comman_prefix=credentials['commandPrefix'])

def getCredentials():
    try:
        credentialsPath = 'msqbitsReporter/msqbitsReporter_discord/ressources/discordsCredentials.json'
        reader = JsonDecryptor.JsonDecryptor()
        reader.chargeJsonFile(credentialsPath)
        return reader.getJsonObject()
    except msqbitsReporterException:
        print('erreur pendant la récupération des credentials')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name = credentials['messageActivity']))
    print("I'm on the case")
        
@bot.event
def on_error(event, *args, **kwargs):
    print('une erreur est survenue')

def run():
    try:
        bot.run(credentials['token'])
    except Exception:
        print('erreur')



