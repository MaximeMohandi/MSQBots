from msqbitsReporter.behavior import news_message, newspaper_manager
import msqbitsReporter.discord.DiscordConnector as discordReporter


bot = discordReporter.bot

@bot.command
async def news(ctx):
    for message in news_message.getArticlesByNewspaper():
        await ctx.send(message)

@bot.command
async def listNp(ctx):
    for message in news_message.getAllNewspapersSaved():
        await ctx.send(message)

@bot.command
async def newsFromCat(ctx, arg):
    pass

@bot.command
async def newsFrom(ctx, arg):
    pass

@bot.command
async def add(ctx, *args):
    pass

@bot.command
async def remove(ctx, arg):
    pass
