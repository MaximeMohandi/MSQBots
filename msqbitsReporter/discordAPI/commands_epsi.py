from msqbitsReporter.behavior import time_table_message
from msqbitsReporter.common import credentials
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime


embedded_color = colour.Colour.dark_blue()
thumbnail_link = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
epsi_footer = "https://beecome.io"


def embed_planning(rawmessage):
    """
    formatting the message in embed style for discord.

    :param rawmessage: a dictionnary representing a message.

    .. seealso:: https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
    .. warning:: This is highly dependents of the time_table_message in the behavior module.
    """
    embed_message = embeds.Embed(
        title=rawmessage['title'],
        colour=embedded_color
    )
    embed_message.set_footer(
        text="si vous trouvez ça long faite savoir à C&D que retourner un html aussi claqué en réponse d'API c'est pas très efficace :)")
    embed_message.set_thumbnail(url=thumbnail_link)
    for fields in rawmessage['courses']:
        embed_message.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=False)
        embed_message.add_field(name=fields['courseteacher'], value=fields['courseroom'], inline=False)

    return embed_message


class EpsiCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.planning_channel = int(credentials.get_credentials('discord')['idEdtChannel'])
        self.display_planning_course_daily.start()

    @commands.command(name='edt', aliases=['timetable', 'planning'],
                      brief='Display planed course',
                      help='Display course programmed for each day nearest the actual week')
    async def display_planning_course(self, ctx):
        await self.__display_planning()

    @tasks.loop(hours=24)
    async def display_planning_course_daily(self):
        weekday = datetime.now().weekday()
        if weekday is 6:
            await self.__display_planning()
        else:
            print('not time for planning')

    async def __display_planning(self):
        for message in time_table_message.getFormatedPlanningWeek():
            await self.bot.get_channel(self.planning_channel).send(embed=embed_planning(message))

    @commands.command(name='daycourse', aliases=['coursefor', 'cours'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        for message in time_table_message.getPlanningFor(arg):
            await ctx.send(embed=embed_planning(message))

    @commands.command(name="todayedt", aliases=['edttoday', 'coursjours'],
                      brief='display course scheduled today')
    async def display_today_planning(self, ctx):
        for message in time_table_message.getThePlanningForToday():
            await ctx.send(embed=embed_planning(message))

    @commands.command(name="nextroom", aliases=['classroom', 'lasalle'],
                      brief="give next classroom")
    async def display_today_next_classroom(self, ctx):
        for message in time_table_message.getRoomNextClassRoom():
            await ctx.send(embed=embed_planning(message))


def setup(bot):
    bot.add_cog(EpsiCommands(bot))
