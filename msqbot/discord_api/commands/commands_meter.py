from meter import meters_control as meter
import exception as msqerror
from discord_api import credentials
from discord.ext import commands
from discord import embeds, colour
import logging

EMBEDDED_COLOR = colour.Colour.dark_purple()
EMBEDDED_FOOTER = "Who's the best ??"
ERROR_NAME = "METER ERROR"


class MeterCommands(commands.Cog):
    """Commands to interact with meter module"""

    def __init__(self, bot):
        self.bot = bot
        self.meter_channel = int(credentials.get_credentials('discord')['idmeterchannel'])
        self.meters = meter.MeterControls()

    @commands.command(name='addmeter', brief='add a new meter')
    async def add_new_meter(self, ctx, *args):
        try:
            name = args[0]
            participants = [self.__get_username_from_tag(arg) for arg in args if '@' in arg]
            rules = args[-1]
            self.meters.create_meter(name, participants, rules)
            await ctx.message.add_reaction('✅')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='rmmeter', brief='remove a meter')
    async def remove_meter(self, ctx, arg):
        try:
            meter_name = arg
            self.meters.remove_meter(meter_name)
            await ctx.message.add_reaction('✅')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='meterlist', brief='Display list of meters')
    async def display_meter_list(self, ctx):
        try:
            meter_list = self.meters.get_all_meters()
            if meter_list:
                message = embeds.Embed(
                    title='METERS LIST',
                    colour=EMBEDDED_COLOR
                )
                message.set_footer(text=EMBEDDED_FOOTER)

                for elt in meter_list:
                    message.add_field(name=elt, value='.', inline=False)

                await self.__send_to_channel__(message, embed=True)
                await ctx.message.add_reaction('✅')
            else:
                await ctx.message.add_reaction('❌')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='meterstatfor', brief='display get meter stat for user')
    async def display_meter_stat_for_user(self, ctx, arg):
        try:
            if arg is not None:
                participant_id = self.__get_username_from_tag(arg)
                participant_summary = self.meters.get_participant_summary(participant_id)
                message = embeds.Embed(
                    title=participant_summary['nom'],
                    colour=EMBEDDED_COLOR
                )
                message.set_footer(text=EMBEDDED_FOOTER)
                message.add_field(name='total score', value=participant_summary['total_score'])
                for elt in participant_summary['meters']:
                    message.add_field(name=elt['name'], value=elt['score'])

                await self.__send_to_channel__(message, embed=True)
                await ctx.message.add_reaction('✅')
            else:
                await ctx.message.add_reaction('❌')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='addpoint', brief='brief score point to user')
    async def add_score_for(self, ctx, *args):
        try:
            meter_name = args[0],
            participant = self.__get_username_from_tag(args[1])
            score = args[2]
            self.meters.update_score(meter_name[0], participant, score)  # args[0] return a tuple
            await ctx.message.add_reaction('✅')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='scoreboard', brief='display scoreboard for meter')
    async def display_scoreboard(self, ctx, arg):
        try:
            await self.__send_scoreboard__(ctx, arg)
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='addplayer', brief='add player to meter')
    async def add_participant_to_meter(self, ctx, *args):
        try:
            participant = self.__get_username_from_tag(args[0])
            meter_name = args[1]
            self.meters.add_participant(participant, meter_name)
            await ctx.message.add_reaction('✅')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='rmplayer', brief='remove player from meter')
    async def remove_participant_from_meter(self, ctx, *args):
        try:
            participant = self.__get_username_from_tag(args[0])
            meter_name = args[1]
            self.meters.remove_participant(participant, meter_name)
            await ctx.message.add_reaction('✅')
        except msqerror.MsqbitsReporterException:
            logging.exception(ERROR_NAME, exc_info=True)
            await ctx.message.add_reaction('❌')

    async def __send_scoreboard__(self, ctx, meter):
        scoreboard = self.meters.get_meter_scoreboard(meter)
        if scoreboard:
            scoreboard_msg = embeds.Embed(
                title=scoreboard['meter'],
                description=scoreboard['rules'],
                colour=EMBEDDED_COLOR
            )
            scoreboard_msg.set_footer(text=EMBEDDED_FOOTER)
            for score in scoreboard['participants']:
                scoreboard_msg.add_field(name=score['name'], value=score['score'], inline=False)
            await self.__send_to_channel__(scoreboard_msg, True)
            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('❌')

    async def __send_to_channel__(self, message, embed=False):
        """Send message to channel

        Parameters
        -----------
            message: :class:`obj`
                message to send in channel
        """
        try:
            if embed is True:
                await self.bot.get_channel(self.meter_channel).send(embed=message)
            else:
                await self.bot.get_channel(self.meter_channel).send(message)

        except Exception as ex:
            logging.error(ex)

    def __get_username_from_tag(self, tag):
        """Transform the user id from the tag

        Parameters
        -----------
            tag: :class:`str`
                user tag
        Returns
        -------
            :class:`str`
                User name
        """
        tag = tag.replace("<", "")
        tag = tag.replace(">", "")
        user_id = tag.replace("@!", "")
        return self.bot.get_user(int(user_id)).name


def setup(bot):
    bot.add_cog(MeterCommands(bot))
