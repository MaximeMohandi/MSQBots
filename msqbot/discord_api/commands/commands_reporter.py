from news_module import newspaper as library, news_errors
from msqbot.discord_api import credentials
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime
import logging

EMBEDDED_COLOR = colour.Colour.dark_red()
THUMBNAIL_LINK = 'https://raw.githubusercontent.com/MaximeMohandi/MSQBitsReporter2.0/master/msqbitsReporter' \
                 '/resources/reporterLogo.png '

NO_NEWSPAPER_ERROR_TEXT = "No newspaper found, check if there's one available"
NO_ARTICLE_ERROR_TEXT = "No Articles found for this newspaper, maybe there's no news today"


def setup(bot):
    bot.add_cog(ReporterCommands(bot))


class ReporterCommands(commands.Cog):
    """Commands to get news from the news module."""
    def __init__(self, bot):
        self.bot = bot
        self.__news_channel_id__ = int(credentials.get_credentials('discord')['idNewsChannel'])
        self.__display_news_daily__.start()
        self.kiosk = library.NewsPaper()

    # commands

    @commands.command(name='addnews', brief='Add a new newspaper',
                      usage='name, web_adresse, rss_link, id_category')
    async def add(self, ctx, *args):
        try:
            if self.__is_empty_args__(args):
                await self.__send_to_channel__("All the parameter has to be filled")
            else:
                result = self.kiosk.add(args[0], args[1], args[2], args[3])
                if result:
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.message.add_reaction('❌')

        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='rmnewspaper', brief='Remove a newspaper',
                      usage='newspaper_name')
    async def remove(self, ctx, arg):
        try:
            if self.__is_empty_args__(arg):
                await self.__send_to_channel__("You didn't give the name of the newspaper you wanted to remove")
            else:
                self.kiosk.remove(arg)
                await ctx.message.add_reaction('✅')

        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='newspapers', brief='Display a list of all the saved newspapers')
    async def display_list_newspapers(self, ctx):
        embed_message = embeds.Embed(title='Available Newspapers', colour=EMBEDDED_COLOR)
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)

        try:
            for newspaper in self.kiosk.get_available():
                embed_message.add_field(
                    name=newspaper['title'],
                    value=newspaper['category'],
                    inline=False
                )
            await self.__send_to_channel__(embed_message, embed=True)

        except news_errors.NoNewspaperFound:
            await self.__send_to_channel__(NO_NEWSPAPER_ERROR_TEXT)
        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='categories', brief='Display a list of all news categories saved')
    async def display_list_categories(self, ctx):
        embed_message = embeds.Embed(title='Available Categories', colour=EMBEDDED_COLOR)
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)

        try:
            for message in self.kiosk.get_categories():
                embed_message.add_field(name=message, value="category", inline=False)

            await self.__send_to_channel__(embed_message, embed=True)

        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='news', brief='Display articles for each newspapers saved in database')
    async def display_news(self, ctx):
        try:
            await self.__display_news__()
        except news_errors.NewsError:
            await ctx.message.add_reaction('❌')

    @commands.command(name='newsby', brief='Display a list of all news by selected category')
    async def display_news_by_category(self, ctx, arg):
        try:
            category = str(arg)
            if self.__is_empty_args__(category):
                await self.__send_to_channel__("You have to give a category name")
            else:
                await self.__send_embedded_news__(self.kiosk.get_news_for_category(category))

        except news_errors.NoNewspaperFound:
            await self.__send_to_channel__(NO_NEWSPAPER_ERROR_TEXT)
            await ctx.message.add_reaction('❌')
        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='newsfor', brief='Display articles from a selected newspaper.')
    async def display_news_by_title(self, ctx, arg):
        try:
            title = str(arg)
            if self.__is_empty_args__(title):
                await self.__send_to_channel__("You have to give a newspaper title")
            else:
                await self.__send_embedded_news__(self.kiosk.get_news_for_newspaper(title))

        except news_errors.NoNewspaperFound:
            await self.__send_to_channel__(NO_NEWSPAPER_ERROR_TEXT)
            await ctx.message.add_reaction('❌')
        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    # private methods

    @tasks.loop(hours=1)
    async def __display_news_daily__(self):
        """Display last news everyday between 9h and 11h"""
        hour = datetime.now().hour
        if 9 <= hour < 11:
            await self.__display_news__()

    async def __display_news__(self):
        """Display last news in Discord embed format"""
        try:
            await self.__send_embedded_news__(self.kiosk.get_last_news())

        except news_errors.NoNewspaperFound:
            await self.__send_to_channel__(NO_NEWSPAPER_ERROR_TEXT)
            raise
        except news_errors.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            raise

    async def __send_embedded_news__(self, newspapers):
        """Send embedded news into channel message

        Parameters
        -----------
            newspapers: :class:`list`
                Discord's dict of newspapers to embed
        """
        for newspaper in newspapers:
            to_send = self.__embed_news__(newspaper)
            await self.__send_to_channel__(to_send, embed=True)

    async def __send_to_channel__(self, message, embed=False):
        """Send message to channel

        Parameters
        -----------
            message: :class:`object`
                Discord's dict of newspapers to embed
        """
        try:
            if embed is True:
                await self.bot.get_channel(self.__news_channel_id__).send(embed=message)
            else:
                await self.bot.get_channel(self.__news_channel_id__).send(message)

        except Exception as ex:
            logging.error(ex)

    def __embed_news__(self, non_embed_msg):
        """formatting the news result to return embedded discord messages

        Parameters
        -----------
            non_embed_msg: :class:`dict`
                Dictionary representing a message

        Notes
        -----
            https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed

        """
        # if one property is None replace by NaN for more flexibility
        message_title = non_embed_msg['title'] if non_embed_msg['title'] is not None else "NaN"
        message_desc = non_embed_msg['description'] if non_embed_msg['description'] is not None else "NaN"
        message_footer = non_embed_msg['website_url'] if non_embed_msg['website_url'] is not None else "NaN"

        embed_message = embeds.Embed(
            title=message_title,
            description=message_desc,
            colour=EMBEDDED_COLOR
        )
        embed_message.set_footer(text=message_footer)
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)
        for article in non_embed_msg['articles']:
            embed_message.add_field(name=article['article_title'], value=article['link'], inline=False)

        return embed_message

    def __is_empty_args__(self, *args):
        """check if a parameter is empty

        Parameters
        -----------
            args: :class:`any`
                method argument to check

        Returns
        -------
            :class:`bool`
                True if an argument is empty
        """
        if len(args) > 0:
            for arg in args:
                if arg is None or len(arg) == 0:
                    return True
            return False
        else:
            return False
