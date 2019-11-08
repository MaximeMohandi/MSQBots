from msqbitsReporter.database import news_database
import feedparser

db = news_database.News()


def get_all_articles():
    newspapers = []
    allNewspaper = db.select_all_newspaper()

    for newsPaper in allNewspaper:
        newspaperarticles = {}

        newspaperarticles['title'] = newsPaper[0]
        newspaperarticles['description'] = newsPaper[2]
        newspaperarticles['footer'] = newsPaper[1]
        newspaperarticles['articles'] = format_articles(newsPaper[3])

        newspapers.append(newspaperarticles)

    return newspapers


def get_saved_newspapers():
    messageStack = []
    allNewpapers = db.select_all_newspaper()

    for newspaper in allNewpapers:
        newspaperdict = {
            'name': "{0} - {1}".format(newspaper[2], newspaper[0]),
            'value': newspaper[1]
        }
        messageStack.append(newspaperdict)

    return messageStack


def get_saved_categories():
    messageStack = []
    allCategories = db.select_categories()

    for category in allCategories:
        messageStack.append("{0} - {1}".format(category[0], category[1]))

    return messageStack


def get_articles_from(newspaper):
    newspapers = []
    allnews = db.select_newspaper_by_name(newspaper)

    if allnews != None:
        newspaperarticles = {
            'title': allnews[1],
            'description': "//",
            'footer': allnews[2],
            'articles': format_articles(allnews[3])
        }
        newspapers.append(newspaperarticles)

    return newspapers


def get_articles_by(category):
    newspapers = []
    allnews = db.select_newspaper_by_cat(category)

    for newsPaper in allnews:
        newspaperarticles = {
            'title': newsPaper[1],
            'description': " ",
            'footer': newsPaper[2],
            'articles': format_articles(allnews[3])
        }

        articles = feedparser.parse(newsPaper[3])
        newspaperarticles['articles'] = format_articles(articles)

    return newspapers


def format_articles(newspaper):
    newspaperarticles = []
    nbarticletoget = 4
    articlecounter = 0

    articles = feedparser.parse(newspaper[3]) # contain the feed link to of the newspaper

    while len(articles.entries) > 0 and articlecounter < nbarticletoget:
        article = articles.entries[articlecounter]
        newspaperarticles.append({
            'titlearticle': article.title,
            'link': article.link,
            'date': article.published
        })
        articlecounter += 1

    return newspaperarticles
