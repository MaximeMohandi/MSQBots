from msqbitsReporter.common import Database
import feedparser

db = Database.Database()

def getArticlesByNewspaper() :
    newspapers = []
    allNewspaper = db.getJournalAll()

    for newsPaper in allNewspaper:
        articleCounter = 0
        newspaperarticles = {}

        newspaperarticles['title'] = newsPaper[0]
        newspaperarticles['description'] = newsPaper[2]
        newspaperarticles['footer'] = newsPaper[1]
        newspaperarticles['articles'] = []

        articles = feedparser.parse(newsPaper[3])
        while len(articles.entries) > 0 and articleCounter < 4:
            article = articles.entries[articleCounter]
            newspaperarticles['articles'].append({
                'titlearticle': article.title,
                'link': article.link,
                'date': article.published
            })
            articleCounter += 1
        newspapers.append(newspaperarticles)
    return newspapers

def getAllNewspapersSaved() :
    messageStack = []
    allNewpapers = db.getJournalAll()

    for newspaper in allNewpapers :
        newspaperdict = {
            'name': "{0} - {1}".format(newspaper[2], newspaper[0]),
            'value': newspaper[1]
        }
        messageStack.append(newspaperdict)
    return messageStack

def getAllCategoriesSaved() :
    messageStack = []
    allCategories = db.getListCategory()

    for category in allCategories :
        messageStack.append("{0} - {1}".format(category[0],category[1]))
    return messageStack

def getAllArticlesFromNewspaper(nomJournal) :
    newspapers = []
    allnews = db.getJournalByNom(nomJournal)
    if allnews != None:
        articleCounter = 0
        newspaperarticles = {}

        newspaperarticles['title'] = allnews[1]
        newspaperarticles['description'] = "//"
        newspaperarticles['footer'] = allnews[2]
        newspaperarticles['articles'] = []

        articles = feedparser.parse(allnews[3])
        while len(articles.entries) > 0 and articleCounter < 4:
            article = articles.entries[articleCounter]
            newspaperarticles['articles'].append({
                'titlearticle': article.title,
                'link': article.link,
                'date': article.published
            })
            articleCounter += 1
        newspapers.append(newspaperarticles)
    return newspapers

def getArticlesFromNewspaperBycat(nomCat):
    newspapers = []
    allnews = db.getJournauxByCat(nomCat)
    for newsPaper in allnews:
        articleCounter = 0
        newspaperarticles = {}

        newspaperarticles['title'] = newsPaper[1]
        newspaperarticles['description'] = " "
        newspaperarticles['footer'] = newsPaper[2]
        newspaperarticles['articles'] = []

        articles = feedparser.parse(newsPaper[3])
        while len(articles.entries) > 0 and articleCounter < 4:
            article = articles.entries[articleCounter]
            newspaperarticles['articles'].append({
                'titlearticle': article.title,
                'link': article.link,
                'date': article.published
            })
            articleCounter += 1
        newspapers.append(newspaperarticles)
    return newspapers
