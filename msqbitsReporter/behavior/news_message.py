from msqbitsReporter.common import Database
import feedparser

db = Database.Database()

def getArticlesByNewspaper() :
    messageStack = []
    allNewspaper = db.getJournalAll()
    articleCounter = 0

    for newsPaper in allNewspaper:
        messageStack.append(
            """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***"""
            .format('\n', newsPaper[0], newsPaper[1], newsPaper[2])
        )
        newsPaperArticles = feedparser.parse(newsPaper[3])

        while(len(newsPaperArticles.entries) > 0 and articleCounter < 4) :
            article = newsPaperArticles.entries[articleCounter]
            messageStack.append(
                """**{0}**\n<{1}>\n*{2}*""".
                format(article.title, article.link, article.published)
            )
            articleCounter+=1
        messageStack.append('\n\n')
    return messageStack

def getAllNewspapersSaved() :
    messageStack = []
    allNewpapers = db.getJournalAll()

    for newspaper in allNewpapers :
        messageStack.append(
            """{0} - {1} : {2} : {3}"""
            .format(newspaper[0], newspaper[1],
                    newspaper[2],newspaper[3])
        )
    messageStack.append('\n\n')
    return messageStack

def getAllCategoriesSaved() :
    messageStack = []
    allCategories = db.getListCategory()

    for category in allCategories :
        messageStack.append(
            """{0} - {1} """
            .format(category[0], category[1])
        )
    messageStack.append('\n\n')
    return messageStack

def getAllArticlesFromNewspaper(nomJournal) :
    messageStack = []
    newspaper = db.getJournalByNom(nomJournal)
    if newspaper != None:
        messageStack.append(
            """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***"""
            .format('\n', newspaper['nom_flux'], newspaper['adresse_flux'], newspaper['categorie_flux'])
        )

        articles = feedparser.parse(newspaper['rss_flux'])
        articleCounter = 0

        while(len(articles.entries) > 0 and articleCounter < 8) :
            article = articles.entries[articleCounter]
            messageStack.append(
                """**{0}**\n<{1}>\n*{2}*""".
                format(article.title, article.link, article.published)
            )
            articleCounter+=1
        messageStack.append('\n\n')
    return messageStack

def getArticlesFromNewspaperBycat(nomCat):
    messageStack = []
    newspapers = db.getJournauxByCat(nomCat)
    if newspapers != None:
        for newspaper in newspapers:
            messageStack.append(
                """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***"""
                .format('\n', newspaper['nom_flux'], newspaper['adresse_flux'], newspaper['categorie_flux'])
            )

            articles = feedparser.parse(newspaper['rss_flux'])
            articleCounter = 0

            while (len(articles.entries) > 0 and articleCounter < 8):
                article = articles.entries[articleCounter]
                messageStack.append(
                    """**{0}**\n<{1}>\n*{2}*""".
                        format(article.title, article.link, article.published)
                )
                articleCounter += 1
        messageStack.append('\n\n')
    return messageStack