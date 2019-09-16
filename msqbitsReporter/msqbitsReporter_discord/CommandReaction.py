import msqbitsReporter.msqbitsReporterException as msqException
import msqbitsReporter.JsonDecryptor as JsonDecryptor
import msqbitsReporter.Database as Database
import msqbitsReporter.msqbitsReporter_discord as discordReporter
import feedparser


db = Database.Database()
json = JsonDecryptor.JsonDecryptor()
bot = discordReporter.bot

@bot.command
async def displayAllNews(self, ctx):
    allNewsPaper = db.getJournalAll()
    for journal in allNewsPaper:
        await ctx.send(
            """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***"""
            .format('\n',journal['nom_flux'],journal['adresse_flux'],journal['categorie_flux'])
        )
        feedReader = feedparser.parse(journal['rss_flux'])
        nbDisplayedArticles = 4
        for articles in feedReader.entries:
            nbDisplayedArticles -= 1
            await ctx.send(
                """**{0}**\n<{1}>\n*{2}*"""
                .format(articles.title,articles.link,articles.published)
            )
            if nbDisplayedArticles == 0:
                break
    return True

@bot.command
async def displayAllJournalsDetails(self, ctx):
    allNewspaper = db.getJournalAll()
    for journal in allNewspaper:
        await ctx.send(
            """{0} - {1} : {2} : {3}"""
            .format(journal['id_flux'], journal['nom_flux'], journal['categorie_flux'], journal['adresse_flux'])
        )
        return True
    pass

@bot.command
async def displayAllNewsFromCat(self, ctx, arg):
    pass

@bot.command
async def displayAllNewsFromJournal(self, ctx, arg):
    pass

@bot.command
async def addNewJournal(self, ctx, *args):
    pass

@bot.command
async def removeJournal(self, ctx, arg):
    pass
