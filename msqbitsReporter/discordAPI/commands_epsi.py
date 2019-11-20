from msqbitsReporter.behavior import time_table_message
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands
from discord import embeds, colour

bot = discordReporter.bot
embededcoulour = colour.Colour.dark_blue()
thumbmaillink = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
embedsepsifooter = "https://beecome.io"


class EpsiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='edt', aliases=['timetable', 'planning'],
                      brief='Display planed course',
                      help='Display course programmed for each day nearest the actual week')
    async def display_planning_course(self, ctx):
        for message in time_table_message.getFormatedPlanningWeek():
            await ctx.send(embed=self.__embed_message(message))

    @commands.command(name='daycourse', aliases=['coursefor', 'cours'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        for message in time_table_message.getPlanningFor(arg):
            await ctx.send(embed=self.__embed_message(message))

    @commands.command(name="todayedt", aliases=['edttoday', 'coursjours'],
                      brief='display course scheduled today')
    async def display_today_planning(self, ctx):
        for message in time_table_message.getThePlanningForToday():
            await ctx.send(embed=self.__embed_message(message))

    @commands.command(name="nextroom", aliases=['classroom', 'lasalle'],
                      brief="give next classroom")
    async def display_today_next_classroom(self, ctx):
        for message in time_table_message.getRoomNextClassRoom():
            await ctx.send(embed=self.__embed_message(message))

    def __embed_message(self, rawmessage):
        """
        formatting the message in embed style for discord.

        :param rawmessage: a dictionnary representing a message.

        .. seealso:: https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
        .. warning:: This is highly dependents of the time_table_message in the behavior module.
        """
        embedmessage = embeds.Embed(
            title=rawmessage['title'],
            colour=embededcoulour
        )
        embedmessage.set_footer(
            text="si vous trouvez ça long faite savoir à C&D que retourner un html aussi claqué en réponse d'API c'est pas très efficace :)")
        embedmessage.set_thumbnail(url=thumbmaillink)
        for fields in rawmessage['courses']:
            embedmessage.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=False)
            embedmessage.add_field(name=fields['courseteacher'], value=fields['courseroom'], inline=False)

        return embedmessage


def setup(bot):
    bot.add_cog(EpsiCommands(bot))
