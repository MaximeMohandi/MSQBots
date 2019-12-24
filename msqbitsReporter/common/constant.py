import os.path as path

CONFIG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources/config.ini')
LOG_FILE = path.join(path.dirname(path.dirname(path.abspath(__file__))), '../logs/log_')
DISCORD_COMMANDS_FILES = ['msqbitsReporter.discord_api.commands_reporter', 'msqbitsReporter.discord_api.commands_epsi',
                          'msqbitsReporter.discord_api.commands_help']
