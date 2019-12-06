from discord.ext import tasks, commands
import asyncio


class AutomatedMessage:
    def __init__(self, bot):
        self.bot = bot
        self.target_channel_id = 565845358261829641

    @tasks.loop(seconds=10)
    async def called_once_a_day(self):
        message_channel = self.bot.get_channel(self.target_channel_id)
        print(f"Got channel {message_channel}")
        await message_channel.send("Your message")

    @called_once_a_day.before_loop
    async def __before(self):
        await self.bot.wait_until_ready()
        print("Finished waiting")


def run_command_every_day_at(funct):
    def wrapper(arg):
        print("this is the function" + funct.__name__)
        print("his argument are " + arg)
