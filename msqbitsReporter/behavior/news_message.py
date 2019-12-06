from msqbitsReporter.database import news_database
import feedparser
import logging

db = news_database.News()
__NB_ARTICLE_TO_GET = 4


def get_all_articles():
    try:
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

    except Exception:
        logging.exception('unable to get all articles', exc_info=True)


def get_saved_newspapers():
    try:
        messageStack = []
        allNewpapers = db.select_all_newspaper()

        for newspaper in allNewpapers:
            newspaperdict = {
                'name': "{0} - {1}".format(newspaper[2], newspaper[0]),
                'value': newspaper[1]
            }
            messageStack.append(newspaperdict)

        return messageStack
    except Exception:
        logging.exception('unable to get saved newspaper', exc_info=True)


def get_saved_categories():
    try:
        messageStack = []
        allCategories = db.select_categories()

        for category in allCategories:
            messageStack.append("{0} - {1}".format(category[0], category[1]))

        return messageStack
    except Exception:
        logging.exception('unable to get savde category', exc_info=True)


def get_articles_from(newspaper):
    try:
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
    except Exception:
        logging.exception(f'unable to get articles from {newspaper}', exc_info=True)

def get_articles_by(category):
    try:
        newspapers = []
        allnews = db.select_newspaper_by_cat(category)
    
        for newsPaper in allnews:
            newspaperarticles = {
                'title': newsPaper[1],
                'description': " ",
                'footer': newsPaper[2],
                'articles': format_articles(newsPaper[3])
            }
    
            articles = feedparser.parse(newsPaper[3])
            newspaperarticles['articles'] = format_articles(articles)
    
        return newspapers
    except Exception:
        logging.exception(f'unable to get articles by {category}', exc_info=True)


def format_articles(feed):
    articles = feedparser.parse(feed)  # contain the feed link to of the newspaper
    try:
        newspaperarticles = []
        articlecounter = 0

        while len(articles.entries) > 0 and articlecounter < __NB_ARTICLE_TO_GET:
            article = articles.entries[articlecounter]
            newspaperarticles.append({
                'titlearticle': article.title,
                'link': article.link,
                'date': article.published
            })
            articlecounter += 1

        return newspaperarticles
    except Exception:
        logging.exception(f'unable to format articles from {feed}', exc_info=True)
