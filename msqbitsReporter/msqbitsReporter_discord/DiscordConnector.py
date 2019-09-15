import asyncio
import discord
from discord.ext import commands
from msqbitsReporter.msqbitsReporterException import msqbitsReporterException
from msqbitsReporter.msqbitsReporter_discord import CommandReaction
import msqbitsReporter.JsonDecryptor as JsonDecryptor



class DiscordClient(discord.Client):
    def __init__(self):
        super(DiscordClient, self).__init__()
        self.getCredentials()
        
        print('init bot')

    def getCredentials(self):
        print('getting credential')
        try:
            credentialsPath = 'msqbitsReporter/msqbitsReporter_discord/ressources/discordsCredentials.json'
            reader = JsonDecryptor.JsonDecryptor()
            reader.chargeJsonFile(credentialsPath)
            credentialsData = reader.getJsonObject()

            self.commandsPrefix = credentialsData['commandPrefix']
            self.TOKEN = credentialsData['token']
            self.messageActivity = credentialsData['messageActivity']
            self.channelId = credentialsData['channelId']
        except msqbitsReporterException:
            print('erreur pendant la récupération des credentials')

    def CommandController(self):
        pass

    @asyncio.coroutine
    def on_ready(self):
        print("I'm on the case")
            
    @asyncio.coroutine
    def on_error(self, event, *args, **kwargs):
        print('une erreur est survenue')

    def run(self):
        print('run')
        message = self.messageActivity
        try:
            super(DiscordClient,self).change_presence(
                activity=discord.Game(name=message)
            )
            super(DiscordClient,self).run(self.TOKEN)
        except Exception:
            print('erreur')



