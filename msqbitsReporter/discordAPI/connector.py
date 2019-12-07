import discord
import logging
from discord.ext import commands
from msqbitsReporter.common import constant, credentials

credentials = credentials.get_credentials('discord')
bot = commands.Bot(command_prefix=credentials['commandPrefix'])


def load_command_files():
    try:
        bot.remove_command('help')
        for file in constant.DISCORD_COMMANDS_FILES:
            bot.load_extension(file)

    except Exception as ex:
        print('error loading extension :')
        print(ex)


def run():
    try:
        logging.basicConfig(level=logging.NOTSET, handlers=[logging.FileHandler(constant.DISCORD_LOG_FILE, 'w', 'utf-8')], format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')
        load_command_files()
        bot.run(credentials['token'], bot=True, reconnect=True)

    except Exception as ex:
        logging.exception(f'unable to run', exc_info=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=credentials['messageActivity']))
    print("I'm on the case")


@bot.event
async def on_error(event, *args, **kwargs):
    print("something append:" + str(event))
    logging.error('something append')


@bot.event
async def on_disconnect():
    logging.info('bot is shutting down')
    print('Bot is shutting down !!')
