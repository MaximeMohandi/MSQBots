import discord
import CommandFunction as cf
import BackgroundTask as bg
import Database as db
from discord.ext import commands


if __name__ == "__main__":
    TOKEN = 'NDA2OTQwNzIyMDc2NTgxOTA4.DU6aaQ.mVXG0L4T3yo1_nMnO_6t1V0j2n0'

activityMessage = "📰"

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('wait..')
    print('it..')
    print('it\'s alive !!!')
    await bot.change_presence(activity=discord.Game(name=activityMessage))
    await bg.GetNewsEveryMorning(bot)

    db.Database.GetCat()

#display feed in channel where it calls
@bot.command(
    brief='Get the last  articles in each feed register in the app',
    help="""if not specified display 4 articles by feed for all category.""",
    usage="number"
    )
async def all(ctx, arg=4):
    await cf.DisplayAll(ctx,arg)

#display a special number of articles for one feed
@bot.command(
    brief='Get a custom number of articles from a specified feed\'s name',
    help="""display a custom number of elements for one feed in the list""",
    usage=""""name" number"""
    )
async def spe(ctx, *args):
    await cf.DisplaySpecial(ctx,args)

#add new feed from user message
@bot.command(
    brief='register a new feed',
    help="""add a new feed in the current list. all the field are mandatory""",
    usage=" \"name\" \"website\" \"feed\" \"category\""
    )
async def add(ctx, *args):
    await cf.AddFeed(ctx,args)

#display the list of feed
@bot.command(
    brief='Get all the feed registered',
    help="""display all the feed registered oredered by category and id. By default it will display all the feed but you can specified a category""",
    usage="category"
    )
async def listflux(ctx,arg='all'):
    await cf.DisplayFeedCategory(ctx,arg)
    
#del a feed from the list
@bot.command(
    brief='remove a registered feed',
    help="remove a feed from the current list. it's recommended to use the command listflux to get the feed id",
    usage="feed's number"
    )
async def delete(ctx,arg):
    await cf.DeleteFeed(ctx,arg)

bot.run(TOKEN)