from epsi_api import planning, exception as epsi_error
import exception as common_error
from msqbot.discord_api import credentials
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
    """Commands to get data from epsi module."""

    def __init__(self, bot):
        self.bot = bot
        self.planning_channel = int(credentials.get_credentials('discord')['idEdtChannel'])
        self.__display_planning_weekly__.start()

    # commands

    @commands.command(name='edt', brief='Display planed course')
    async def display_planning_week(self, ctx):
        await self.__display_planning__()

    @commands.command(name='edtfor', brief='Display planed course for given day')
    async def display_planning_for_date(self, ctx, arg):
        try:
            date = arg
            for message in planning.get_courses_for(date):
                await self.__send_embed_planning__(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)
            await ctx.message.add_reaction('❌')
        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)
            await ctx.message.add_reaction('❌')

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
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)
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
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)
            await ctx.message.add_reaction('❌')

    # private methods

    @tasks.loop(hours=24)
    async def __display_planning_weekly__(self):
        """ Send EPSI planning every sunday."""
        weekday = datetime.now().weekday()
        if weekday is 6:
            await self.__display_planning__()

    async def __display_planning__(self):
        """ Send planning entire planning for the week."""
        try:
            for message in planning.get_week_courses():
                await self.__send_embed_planning__(message)

        except epsi_error.ParserNoPlanningFound:
            await self.__send_text__(NO_PLANNING_FOUND_MESSAGE)

        except (common_error.HttpError, epsi_error.EpsiError):
            await self.__send_text__(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

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
