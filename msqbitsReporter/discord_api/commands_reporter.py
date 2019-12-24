from msqbitsReporter.database import news_database as db
from msqbitsReporter.behavior import news_message
from msqbitsReporter.common import credentials
from discord.ext import commands, tasks
from discord import embeds, colour
from datetime import datetime
import logging

db = db.News()
EMBEDDED_COLOR = colour.Colour.dark_red()
THUMBNAIL_LINK = 'https://raw.githubusercontent.com/MaximeMohandi/MSQBitsReporter2.0/master/msqbitsReporter' \
                 '/resources/reporterLogo.png '


def setup(bot):
    bot.add_cog(ReporterCommands(bot))


class ReporterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.news_channel = int(credentials.get_credentials('discord')['idNewsChannel'])
        self.display_x_news_daily.start()

    @commands.command(name='newspapers',
                      brief='Display a list of all the saved newspapers',
                      help='Display a list of all the saved newspapers with their ID and their titles. Useful'
                           'to then get articles for a specific newspaper')
    async def display_list_newspapers(self, ctx):
        embed_message = embeds.Embed(
            title='Newspapers List',
            colour=EMBEDDED_COLOR
        )
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)
        for message in news_message.get_saved_newspapers():
            embed_message.add_field(name=message['name'], value=message['value'], inline=False)

        await self.__send_to_news_channel(embed_message)

    @commands.command(name='categories',
                      brief='Display a list of all news categories saved',
                      help='Display a list of all news categories saved with their ID and their titles. Useful'
                           'to then get news from a specific category')
    async def display_list_categories(self, ctx):
        embed_message = embeds.Embed(
            title='Category List',
            colour=EMBEDDED_COLOR
        )
        embed_message.set_thumbnail(url=THUMBNAIL_LINK)
        for message in news_message.get_saved_categories():
            embed_message.add_field(name=message, value="category", inline=False)

        await self.__send_to_news_channel(embed_message)

    @commands.command(name='news',
                      brief='Display last four articles for each newspapers saved in database',
                      help='Display last four articles for each newspapers saved in database, this command'
                           'can be stop by typing $stop at anytime.')
    async def display_x_news(self, ctx):
        await self.__display_news()

    @tasks.loop(hours=2)
    async def display_x_news_daily(self):
        hour = datetime.now().hour

        if 9 <= hour < 11:
            await self.__display_news()
        else:
            print('not time for news')

    async def __display_news(self):
        for message in news_message.get_all_articles():
            await self.__send_to_news_channel(embed_news(message))

    @commands.command(name='newscat',
                      brief='Display a list of all news by selected category',
                      help='Display a list of all news by selected category, this command can be'
                           'by typing $stop')
    async def display_news_by_category(self, ctx, arg):
        for message in news_message.get_articles_by(arg):
            await self.__send_to_news_channel(embed_news(message))

    @commands.command(name='newsdaily',
                      brief='Display articles from a selected newspaper.',
                      help='Display 8 articles from a selected newspaper. This command can be stopped by typing $stop')
    async def display_news_by_newspaper(self, ctx, arg):
        for message in news_message.get_articles_from(arg):
            await self.__send_to_news_channel(embed_news(message))

    async def __send_to_news_channel(self, message):
        try:
            await self.bot.get_channel(self.news_channel).send(embed=message)
        except Exception as ex:
            logging.error(ex)

    @commands.command(name='addnewspaper',
                      brief='Add a new newspaper',
                      help='Add a new newspaper, all the arguments are mandatory !',
                      usage='name, web_adresse, rss_link, id_category')
    async def add(self, ctx, *args):
        try:
            db.insert_newspaper(args[0], args[1], args[2], args[3])
            await ctx.message.add_reaction('✅')
        except Exception as ex:
            print(ex)
            logging.exception('unable to add newspaper', exc_info=True)
            await ctx.message.add_reaction('❌')

    @commands.command(name='removenewspaper',
                      brief='Remove a newspaper',
                      help='Remove a newspaper from the database',
                      usage='newspaper_name')
    async def remove(self, ctx, arg):
        try:
            db.delete_newspaper(arg)
            await ctx.message.add_reaction('✅')

        except Exception:
            print(Exception)
            logging.exception('unable to remove newspaper', exc_info=True)
            await ctx.message.add_reaction('❌')




def embed_news(non_embed_msg):
    """
        formatting the news result to return embedded discord messages

        :param non_embed_msg: a dictionnary representing a message.

        .. seealso:: https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
        .. warning:: This is highly dependents of the news return
    """
    # if one property is None replace by None for more flexibility
    message_title = non_embed_msg['title'] if non_embed_msg['title'] is not None else "NaN"
    message_desc = non_embed_msg['description'] if non_embed_msg['description'] is not None else "NaN"
    message_footer = non_embed_msg['footer'] if non_embed_msg['footer'] is not None else "NaN"

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
