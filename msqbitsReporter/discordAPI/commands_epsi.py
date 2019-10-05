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
        for message in time_table_message.getPlanningWeek():
            await ctx.send(message)

    @commands.command(name='whatcourse', aliases=['coursefor', 'onaquoile'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        for message in time_table_message.getPlanningFor(arg):
            await ctx.send(message)

    @commands.command(name="todayedt", aliases=['today','edtaujourdhui'],
                      brief='display course scheduled today')
    async def display_today_planning(self,ctx):
        for message in time_table_message.getThePlanningForToday():
            await ctx.send(message)

    @commands.command(name="nextroom", aliases=['classroom','lasalle'],
                      brief="give next classroom")
    async def display_today_next_classroom(self,ctx):
        for message in time_table_message.getRoomNextClassRoom():
            await ctx.send(message)

def setup(bot):
    bot.add_cog(EpsiCommands(bot))