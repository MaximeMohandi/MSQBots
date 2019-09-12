import msqbitsReporter.msqbitsReporterException as msqException
import msqbitsReporter.JsonDecryptor as JsonDecryptor
import msqbitsReporter.Database as Database
import feedparser

db = Database.Database()
json = JsonDecryptor.JsonDecryptor()

async def displayAllNews(ctx, arg):
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
        
async def displayAllJournalsDetails(ctx, arg):
    allNewspaper = db.getJournalAll()
    for journal in allNewspaper:
        await ctx.send(
            """{0} - {1} : {2} : {3}"""
            .format(journal['id_flux'], journal['nom_flux'], journal['categorie_flux'], journal['adresse_flux'])
        )
        return True
    pass

async def displayAllNewsFromCat(ctx, arg):
    #display list of journal from a defined category
    pass

async def displayAllNewsFromJournal(ctx, arg):
    #display a limited but larger amount of articles from an unique journal (define the amount in arg with a limited number)
    pass

async def addNewJournal(ctx, *args):
    #add a journal to the database
    pass

async def removeJournal(ctx, arg):
    #remove a journal from an id
    pass
