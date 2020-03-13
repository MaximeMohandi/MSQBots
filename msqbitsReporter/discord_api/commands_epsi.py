from msqbitsReporter.epsi_api import time_table_api as time_table, exception as epsi_error
from msqbitsReporter.common import credentials, exception as common_error
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime
import logging


EMBEDDED_COLOR = colour.Colour.dark_blue()
THUMBNAIL_LINK = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
EMBED_FOOTER = "https://beecome.io"

NO_PLANNING_FOUND_MESSAGE = "It seems that nothing is planned"
ERROR_MESSAGE = "hmm something happened, check the logs for more details"


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
        try:
            for message in time_table.get_week_planning():
                await self.__send_embed_planning(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

    @commands.command(name='daycourse', aliases=['coursefor', 'cours'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        try:
            for message in time_table.get_planning_for(arg):
                await self.__send_embed_planning(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

    @commands.command(name="todayedt", aliases=['edttoday', 'coursjours'],
                      brief='display course scheduled today')
    async def display_today_planning(self, ctx):
        try:
            for message in time_table.get_today_planning():
                await self.__send_embed_planning(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

    @commands.command(name="nextroom", aliases=['classroom', 'lasalle'],
                      brief="give next classroom")
    async def display_today_next_classroom(self, ctx):
        try:
            for message in time_table.get_next_classroom():
                await self.__send_embed_planning(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

    async def __send_embed_planning(self, rawmessage):
        embed_message = embeds.Embed(
            title=rawmessage['title'],
            colour=EMBEDDED_COLOR
        )
        embed_message.set_footer(
            text="si vous trouvez ça long faite savoir à C&D que retourner un html aussi claqué en réponse d'API c'est pas très efficace :)")
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)
        for fields in rawmessage['courses']:
            hours = '{} - {}'.format(fields['hourscourse'][0], fields['hourscourse'][1])
            embed_message.add_field(name=hours, value=fields['courselabel'], inline=False)
            embed_message.add_field(name=fields['courseteacher'], value=fields['courseroom'], inline=False)

        await self.bot.get_channel(self.planning_channel).send(embed=embed_message)

    async def __send_text(self, message):
        await self.bot.get_channel(self.planning_channel).send(message)


def setup(bot):
    bot.add_cog(EpsiCommands(bot))
