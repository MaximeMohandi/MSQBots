from msqbitsReporter.behavior import news_message as newspaper
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands

bot = discordReporter.bot

class ReporterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='getNews', aliases=['allNews', 'nouvelles'],
                      brief='Display last four articles for each newspapers saved in database',
                      help='Display last four articles for each newspapers saved in database, this command'
                           'can be stop by typing $stop at anytime.')
    async def display_x_news_by_newspapers(self, ctx):
        for message in newspaper.getArticlesByNewspaper():
            await ctx.send(message)

    @commands.command(name='getNewspapers', aliases=['newspapers', 'journaux'],
                      brief='Display a list of all the saved newspapers',
                      help='Display a list of all the saved newspapers with their ID and their titles. Useful'
                           'to then get articles for a specific newpaper')
    async def display_list_newspapers(self, ctx):
        for message in newspaper.getAllNewspapersSaved():
            await ctx.send(message)

    @commands.command(name='getCategories', aliases=['categories', 'catégories'],
                      brief='Display a list of all news categories saved',
                      help='Display a list of all news categories saved with their ID and their titles. Useful'
                           'to then get news from a specific category')
    async def display_list_categories(self, ctx):
        for message in newspaper.getAllCategoriesSaved():
            await ctx.send(message)

    @commands.command(name='getNewsBy', aliases=['newsBy', 'parCatégories'],
                      brief='Display a list of all news by selected category',
                      help='Display a list of all news by selected category, this command can be'
                           'by typing $stop')
    async def display_news_by_category(self, ctx, arg):
        for message in newspaper.getArticlesFromNewspaperBycat(arg):
            await ctx.send(message)

    @commands.command(name='')
    async def newsFrom(ctx, arg):
        pass

    @bot.command
    async def add(ctx, *args):
        pass

    @bot.command
    async def remove(ctx, arg):
        pass

def setup(bot):
    bot.add_cog(ReporterCommands(bot))