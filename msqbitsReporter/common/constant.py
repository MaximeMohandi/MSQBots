import os.path as path

DATABASE_CREDENTIALS_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'ressources/databaseParameter.json')
DISCORD_CREDENTIALS_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'ressources/discordsCredentials.json')
DISCORD_LOG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'ressources/discord_api.log')
DISCORD_COMMANDS_FILES = ['discordAPI.commands_reporter', 'discordAPI.commands_epsi']