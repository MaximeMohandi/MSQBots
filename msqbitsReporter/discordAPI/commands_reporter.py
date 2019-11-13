from msqbitsReporter.behavior import news_message
from msqbitsReporter.database import news_database as db
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands
from discord import embeds, colour
import logging

db = db.News()
bot = discordReporter.bot
embededcoulour = colour.Colour.dark_red()
thumbmaillink = 'https://raw.githubusercontent.com/MaximeMohandi/MSQBitsReporter2.0/master/msqbitsReporter/ressources/reporterLogo.png'

class ReporterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='news',
                      brief='Display last four articles for each newspapers saved in database',
                      help='Display last four articles for each newspapers saved in database, this command'
                           'can be stop by typing $stop at anytime.')
    async def display_x_news(self, ctx):
        for message in news_message.get_all_articles():
            embedmessage = embeds.Embed(
                title=message['title'],
                description=message['description'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=message['footer'])
            embedmessage.set_thumbnail(url=thumbmaillink)
            for article in message['articles']:
                embedmessage.add_field(name=article['titlearticle'], value=article['link'])

            await ctx.send(embed=embedmessage)

    @commands.command(name='newspapers',
                      brief='Display a list of all the saved newspapers',
                      help='Display a list of all the saved newspapers with their ID and their titles. Useful'
                           'to then get articles for a specific newpaper')
    async def display_list_newspapers(self, ctx):
        newspaperslist = news_message.get_saved_newspapers()
        embedmessage = embeds.Embed(
            title='Newspapers List',
            colour=embededcoulour
        )
        embedmessage.set_thumbnail(url=thumbmaillink)
        for message in newspaperslist:
            embedmessage.add_field(name=message['name'], value=message['value'], inline=False)

    @commands.command(name='categories',
                      brief='Display a list of all news categories saved',
                      help='Display a list of all news categories saved with their ID and their titles. Useful'
                           'to then get news from a specific category')
    async def display_list_categories(self, ctx):
        newspaperslist = news_message.get_saved_categories()
        embedmessage = embeds.Embed(
            title='Category List',
            colour=embededcoulour
        )
        embedmessage.set_thumbnail(url=thumbmaillink)
        for message in newspaperslist:
            embedmessage.add_field(name=message, value="category", inline=False)

        await ctx.send(embed=embedmessage)

    @commands.command(name='newscat',
                      brief='Display a list of all news by selected category',
                      help='Display a list of all news by selected category, this command can be'
                           'by typing $stop')
    async def display_news_by_category(self, ctx, arg):
        for message in news_message.get_articles_by(arg):
            embedmessage = embeds.Embed(
                title=message['title'],
                description=message['description'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=message['footer'])
            embedmessage.set_thumbnail(url=thumbmaillink)
            for article in message['articles']:
                embedmessage.add_field(name=article['titlearticle'], value=article['link'])

            await ctx.send(embed=embedmessage)

    @commands.command(name='newsdaily',
                      brief='Display articles from a selected newspaper.',
                      help='Display 8 articles from a selected newspaper. This command can be stopped by typing $stop')
    async def display_news_by_newspaper(self, ctx, arg):
        for message in news_message.get_articles_from(arg):
            embedmessage = embeds.Embed(
                title=message['title'],
                description=message['description'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=message['footer'])
            embedmessage.set_thumbnail(url=thumbmaillink)
            for article in message['articles']:
                embedmessage.add_field(name=article['titlearticle'], value=article['link'])

            await ctx.send(embed=embedmessage)

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


def setup(bot):
    bot.add_cog(ReporterCommands(bot))
