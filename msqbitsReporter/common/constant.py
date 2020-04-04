import os.path as path

RESOURCE_FOLDER_PATH = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources/')
CONFIG_FILE = RESOURCE_FOLDER_PATH + 'config.ini'
DATABASE_FILE = RESOURCE_FOLDER_PATH + 'msqbreporter_database.db'
LOG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), '../logs/log_')
DISCORD_COMMANDS_FILES = ['msqbitsReporter.discord_api.commands_reporter',
                          'msqbitsReporter.discord_api.commands_epsi',
                          'msqbitsReporter.discord_api.commands_corona',
                          'msqbitsReporter.discord_api.commands_help',
                          ]
