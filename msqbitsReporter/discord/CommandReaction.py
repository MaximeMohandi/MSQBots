from msqbitsReporter.behavior import news_message, newspaper_manager
import msqbitsReporter.discord.DiscordConnector as discordReporter


bot = discordReporter.bot

@bot.command
async def displayAllNews(ctx):
    for message in news_message.getArticlesByNewspaper():
        await ctx.send(message)

@bot.command
async def displayAllJournalsDetails(ctx):
    for message in news_message.getAllNewspapersSaved():
        await ctx.send(message)

@bot.command
async def displayAllNewsFromCat(ctx, arg):
    pass

@bot.command
async def displayAllNewsFromJournal(ctx, arg):
    pass

@bot.command
async def addNewJournal(ctx, *args):
    pass

@bot.command
async def removeJournal(ctx, arg):
    pass
