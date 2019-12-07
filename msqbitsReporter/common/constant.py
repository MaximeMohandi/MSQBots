import os.path as path

CONFIG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources/config.ini')
LOG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), '../logs/log_')
DISCORD_COMMANDS_FILES = ['msqbitsReporter.discordAPI.commands_reporter', 'msqbitsReporter.discordAPI.commands_epsi',
                          'msqbitsReporter.discordAPI.commands_help']
