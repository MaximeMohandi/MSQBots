from msqbitsReporter.behavior import time_table_message
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands

bot = discordReporter.bot

class EpsiCommands(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='planning', aliases=['timetable', 'edt'],
                      brief='Display planed course',
                      help='Display course programmed for each day nearest the actual week')
    async def display_planning_course(self, ctx):
        await ctx.send('*This is a BETA feature, to report issues : <https://github.com/MaximeMohandi/MSQBitsReporter2.0/issues>*') #TODO delete this when it's fully operational
        for message in time_table_message.getPlanningWeek():
            await ctx.send(message)

def setup(bot):
    bot.add_cog(EpsiCommands(bot))