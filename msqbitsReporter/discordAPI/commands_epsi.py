from msqbitsReporter.behavior import time_table_message
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands
from datetime import datetime

bot = discordReporter.bot

class EpsiCommands(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='planning', aliases=['timetable', 'edt'],
                      brief='Display planed course',
                      help='Display course programmed for each day nearest the actual week')
    async def display_planning_course(self, ctx):
        await self.disclaimer_msg(ctx)
        for message in time_table_message.getPlanningWeek():
            await ctx.send(message)

    @commands.command(name='whatcourse', aliases=['coursefor', 'onaquoile'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        await self.disclaimer_msg(ctx)
        for message in time_table_message.getPlanningFor(arg):
            await ctx.send(message)

    @commands.command(name="todayedt", aliases=['today','edtajourdhui'],
                      brief='display course scheduled today')
    async def display_today_planning(self,ctx):
        await self.disclaimer_msg(ctx)
        for message in time_table_message.getPlanningFor(datetime.today()):
            await ctx.send(message)

    async def disclaimer_msg(self,ctx):
        await ctx.send(
            'This is a BETA feature, to report issues : <https://github.com/MaximeMohandi/MSQBitsReporter2.0/issues>')  # TODO delete this when it's fully operational


def setup(bot):
    bot.add_cog(EpsiCommands(bot))