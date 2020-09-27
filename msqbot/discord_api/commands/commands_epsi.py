from epsi_api import planning, exception as epsi_error
import exception as common_error
from msqbot.discord_api import credentials
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime, timedelta
import logging

EMBEDDED_COLOR = colour.Colour.dark_blue()
THUMBNAIL_LINK = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
EMBED_FOOTER = "https://beecome.io"

NO_PLANNING_FOUND_MESSAGE = "It seems that nothing is planned"
ERROR_MESSAGE = "hmm something happened, check the logs for more details"
PARSING_ERROR = "Something got wrong with the parsing of time table website"


class EpsiCommands(commands.Cog):
    """Commands to get data from epsi module."""

    def __init__(self, bot):
        self.bot = bot
        self.planning_channel = int(credentials.get_credentials('discord')['idEdtChannel'])
        self.__display_planning_weekly__.start()

    # ===================================
    # COMMANDS
    # ==================================
    @commands.command(name='edt', brief='Display planed course')
    async def display_planning_week(self, ctx, arg=None):
        if arg is None:
            await self.__display_planning__()
        else:
            await self.__display_planning_for_date__(arg)

    @commands.command(name="edttoday", brief='display course scheduled today')
    async def display_today_planning(self, ctx):
        try:
            for message in planning.get_today_courses():
                await self.__send_embed_planning__(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)
            await ctx.message.add_reaction('❌')
        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception(PARSING_ERROR, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name="nextroom", brief="give next classroom")
    async def display_today_next_classroom(self, ctx):
        try:
            await self.__send_text__(planning.get_next_classroom())

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)
            await ctx.message.add_reaction('❌')
        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception(PARSING_ERROR, exc_info=True)
            await ctx.message.add_reaction('❌')

    # ===================================
    # PRIVATE METHODS
    # ==================================

    @tasks.loop(hours=2)
    async def __display_planning_weekly__(self):
        """ Send EPSI planning for next week every friday between 4pm and 6 pm."""
        today = datetime.now()
        if today.weekday() == 4:
            if 16 <= datetime.now().hour <= 18:
                await self.__display_planning_for_date__(today + timedelta(days=3))  # set date to the next monday

    async def __display_planning__(self):
        """ Send planning entire planning for the week."""
        try:
            for message in planning.get_week_courses():
                await self.__send_embed_planning__(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception(PARSING_ERROR, exc_info=True)

    async def __display_planning_for_date__(self, date):
        """ Send planning for the week which contain the given date"""
        try:
            for message in planning.get_week_courses_for(date):
                await self.__send_embed_planning__(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)
        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception(PARSING_ERROR, exc_info=True)

    async def __send_embed_planning__(self, rawmessage):
        """Format the raw planning into a embed message for discord"""
        embed_message = embeds.Embed(
            title=rawmessage['title'],
            colour=EMBEDDED_COLOR
        )
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)
        for fields in rawmessage['courses']:
            hours = '{} - {}'.format(fields['hourscourse'][0], fields['hourscourse'][1])
            embed_message.add_field(name=hours, value=fields['courselabel'], inline=False)
            embed_message.add_field(name=fields['courseteacher'], value=fields['courseroom'], inline=False)

        await self.bot.get_channel(self.planning_channel).send(embed=embed_message)

    async def __send_text__(self, message):
        """The a unique message without format."""
        await self.bot.get_channel(self.planning_channel).send(message)


def setup(bot):
    bot.add_cog(EpsiCommands(bot))
