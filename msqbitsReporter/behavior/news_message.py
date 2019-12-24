from msqbitsReporter.database import news_database
import feedparser
import logging

db = news_database.News()
__NB_ARTICLE_TO_GET = 4


def get_all_articles():
    try:
        newspapers = []
        all_newspaper = db.select_all_newspaper()

        for newsPaper in all_newspaper:
            newspaper_articles = {'title': newsPaper[0], 'description': newsPaper[2],
                                  'footer': newsPaper[1], 'articles': format_articles(newsPaper[3])}

            newspapers.append(newspaper_articles)

        return newspapers

    except Exception :
        logging.exception('unable to get all articles', exc_info=True)


def get_saved_newspapers():
    try:
        message_stack = []
        all_newspapers = db.select_all_newspaper()

        for newspaper in all_newspapers:
            newspaperdict = {
                'name': "{0} - {1}".format(newspaper[2], newspaper[0]),
                'value': newspaper[1]
            }
            message_stack.append(newspaperdict)

        return message_stack
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
        all_news = db.select_newspaper_by_name(newspaper)

        if all_news != None:
            newspaper_articles = {
                'title': all_news[1],
                'description': "//",
                'footer': all_news[2],
                'articles': format_articles(all_news[3])
            }
            newspapers.append(newspaper_articles)

        return newspapers
    except Exception:
        logging.exception(f'unable to get articles from {newspaper}', exc_info=True)


def get_articles_by(category):
    try:
        newspapers = []
        all_news = db.select_newspaper_by_cat(category)

        for newsPaper in all_news:
            newspaper_articles = {
                'title': newsPaper[1],
                'description': " ",
                'footer': newsPaper[2],
                'articles': format_articles(newsPaper[3])
            }

            articles = feedparser.parse(newsPaper[3])
            newspaper_articles['articles'] = format_articles(articles)

        return newspapers
    except Exception:
        logging.exception(f'unable to get articles by {category}', exc_info=True)


def format_articles(feed):
    articles = feedparser.parse(feed)  # contain the feed link to of the newspaper
    try:
        newspaper_articles = []
        articles_counter = 0

        while len(articles.entries) > 0 and articles_counter < __NB_ARTICLE_TO_GET:
            article = articles.entries[articles_counter]
            newspaper_articles.append({
                'titlearticle': article.title,
                'link': article.link,
                'date': article.published
            })
            articles_counter += 1

        return newspaper_articles
    except Exception:
        logging.exception(f'unable to format articles from {feed}', exc_info=True)
