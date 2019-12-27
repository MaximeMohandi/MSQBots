from msqbitsReporter.news import news_local_db as db, exception as news_error
from msqbitsReporter.common import credentials
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime
import logging

db = db.LocalDatabase()
EMBEDDED_COLOR = colour.Colour.dark_red()
THUMBNAIL_LINK = 'https://raw.githubusercontent.com/MaximeMohandi/MSQBitsReporter2.0/master/msqbitsReporter' \
                 '/resources/reporterLogo.png '

NO_NEWSPAPER_ERROR_TEXT = "No newspaper found, check if there's one available"
NO_ARTICLE_ERROR_TEXT = "No Articles found for this newspaper, maybe there's no news today"


def setup(bot):
    bot.add_cog(ReporterCommands(bot))


class ReporterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__news_channel_id = int(credentials.get_credentials('discord')['idNewsChannel'])
        self.display_news_daily.start()

    @commands.command(name='addnews', brief='Add a new newspaper',
                      help='Add a new newspaper, all the arguments are mandatory !',
                      usage='name, web_adresse, rss_link, id_category')
    async def add(self, ctx, *args):
        try:
            if self.__is_empty_arg(args):
                await self.__send_to_news_channel("All the parameter has to be filled")
            else:
                db.insert_newspaper(args[0], args[1], args[2], args[3])
                await ctx.message.add_reaction('✅')

        except (news_error.LocalDatabaseError, news_error.RssParsingError):
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='removenewspaper',
                      brief='Remove a newspaper',
                      help='Remove a newspaper from the database',
                      usage='newspaper_name')
    async def remove(self, ctx, arg):
        try:
            if self.__is_empty_arg(arg):
                await self.__send_to_news_channel("You didn't give the name of the newspaper you wanted to remove")
            else:
                db.delete_newspaper(arg)
                await ctx.message.add_reaction('✅')

        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='newspapers',
                      brief='Display a list of all the saved newspapers',
                      help='Display a list of all the saved newspapers with their ID and their titles. Useful'
                           'to then get articles for a specific newspaper')
    async def display_list_newspapers(self, ctx):
        embed_message = embeds.Embed(title='Available Newspaper', colour=EMBEDDED_COLOR)
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)

        try:
            for message in db.select_newspaper():
                embed_message.add_field(name=message['title'], value=message['website_url'], inline=False)
            await self.__send_to_news_channel(embed_message, embed=True)

        except news_error.NoNewspaperFound:
            await self.__send_to_news_channel(NO_NEWSPAPER_ERROR_TEXT)
        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)

    @commands.command(name='categories',
                      brief='Display a list of all news categories saved',
                      help='Display a list of all news categories saved with their ID and their titles. Useful'
                           'to then get news from a specific category')
    async def display_list_categories(self, ctx):
        embed_message = embeds.Embed(title='Available Categories', colour=EMBEDDED_COLOR)
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)

        try:
            for message in db.select_categories():
                embed_message.add_field(name=message, value="category", inline=False)

            await self.__send_to_news_channel(embed_message, embed=True)
        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)

    @commands.command(name='news',
                      brief='Display articles for each newspapers saved in database',
                      help='Display last four articles for each newspapers saved in database, this command'
                           'can be stop by typing $stop at anytime.')
    async def display_news(self, ctx):
        await self.__display_news()

    @tasks.loop(hours=2)
    async def display_news_daily(self):
        hour = datetime.now().hour

        if 9 <= hour < 11:
            await self.__display_news()
        else:
            print('not time for news')

    async def __display_news(self):
        try:
            await self.__send_embedded_news(db.select_newspaper())

        except news_error.NoNewspaperFound:
            await self.__send_to_news_channel(NO_NEWSPAPER_ERROR_TEXT)
        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)

    @commands.command(name='newscat',
                      brief='Display a list of all news by selected category',
                      help='Display a list of all news by selected category, this command can be'
                           'by typing $stop')
    async def display_news_by_category(self, ctx, arg):
        try:
            if self.__is_empty_arg(arg):
                await self.__send_to_news_channel("You have to give a category name")
            else:
                await self.__send_to_news_channel(db.select_newspaper_by_cat(arg))

        except news_error.NoNewspaperFound:
            await self.__send_to_news_channel(NO_NEWSPAPER_ERROR_TEXT)
        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)

    @commands.command(name='newsfortitle',
                      brief='Display articles from a selected newspaper.',
                      help='Display 8 articles from a selected newspaper. This command can be stopped by typing $stop')
    async def display_news_by_title(self, ctx, arg):
        try:
            if self.__is_empty_arg(arg):
                await self.__send_to_news_channel("You have to give a newspaper title")
            else:
                await self.__send_embedded_news(db.select_newspaper_by_title(arg))

        except news_error.NoNewspaperFound:
            await self.__send_to_news_channel(NO_NEWSPAPER_ERROR_TEXT)
        except news_error.NewsError:
            logging.exception('NEWS_ERROR', exc_info=True)

    # private method

    async def __send_embedded_news(self, newspapers):
        for newspaper in newspapers:
            to_send = self.__embed_news(newspaper)
            await self.__send_to_news_channel(to_send, embed=True)

    async def __send_to_news_channel(self, message, embed=False):
        try:
            if embed is True:
                await self.bot.get_channel(self.__news_channel_id).send(embed=message)
            else:
                await self.bot.get_channel(self.__news_channel_id).send(message)

        except Exception as ex:
            logging.error(ex)

    def __embed_news(self, non_embed_msg):
        """
            formatting the news result to return embedded discord messages

            :param non_embed_msg: a dictionnary representing a message.
            :type non_embed_msg: dict

            .. seealso:: https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
            .. warning:: This is highly dependents of the news return
        """
        # if one property is None replace by None for more flexibility
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
            embed_message.add_field(name=article['titlearticle'], value=article['link'], inline=False)

        return embed_message

    def __is_empty_arg(self, *args):
        """
            check if a parameter is empty

            :param args: method argument to check
            :type args: any

            :returns: True if an argument is empty
            :rtype: bool
        """
        if len(args) > 0:
            for arg in args:
                if arg is None or len(arg) == 0:
                    return True
            return False
        else:
            return False
