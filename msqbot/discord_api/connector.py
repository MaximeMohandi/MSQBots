import logging
import constant
import discord
from discord_api import credentials
from discord.ext import commands
from datetime import datetime


DISCORD_COMMANDS_FILES = [
    'msqbot.discord_api.commands.commands_epsi',
    'msqbot.discord_api.commands.commands_meter'
]


credentials = credentials.get_credentials('discord')
bot = commands.Bot(command_prefix=credentials['command_prefix'])


def create_log_file():
    logfile = 'log_{}.log'.format(str(datetime.now().strftime("%m%d%Y%H%M%S")))
    logging.basicConfig(level=logging.INFO,
                        handlers=[logging.FileHandler(constant.LOG_FILE + logfile, 'w', 'utf-8')],
                        format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')


def load_command_files():
    try:
        for file in DISCORD_COMMANDS_FILES:
            bot.load_extension(file)

        logging.info("command_loaded")

    except Exception as ex:
        print(ex)
        logging.exception(f'error loading extension', exc_info=True)


def run():
    try:
        create_log_file()
        load_command_files()
        bot.run(credentials['token'], bot=True, reconnect=True)

    except Exception:
        logging.exception(f'unable to run', exc_info=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=credentials['message_activity']))
    print("I'm on the case")
    logging.info("bot running")


@bot.event
async def on_error(event, *args, **kwargs):
    print("something append:" + str(event))
    logging.error('something append')


@bot.event
async def on_disconnect():
    logging.info('bot is shutting down')
    print('Bot is shutting down !!')
