from news import news_errors, news_local_db
import feedparser


class NewsPaper:
    """Function to manage library of newspaper"""

    def __init__(self):
        self.__NB_ARTICLE_MAX = 10
        self.database = news_local_db.LocalDatabase()

    def add(self, title, website, rss_link, category_name):
        """Add a newspaper into the library

        Parameters
        -----------
            title: :class:`str`
                newspaper title
            website: :class:`str`
                newspaper website url
            rss_link: :class:`str`
                newspaper rss feed
            category_name: :class:`str`
                newspaper category

        Returns
        -------
            :class:`bool`
                Status of query

        Raises
        -------
            NewsError
                An error occurred when adding newspaper
        """
        try:
            insertion_result = self.database.insert_newspaper(title, website, rss_link, category_name)
            return False if insertion_result is None else True
        except Exception:
            raise news_errors.NewsError

    def remove(self, title):
        """Remove the newspaper with the given name

        Parameters
        -----------
            title: :class:`str`
                name of the newspaper to remove

        Raises
        -------
            NewsError
                An error occurred when adding newspaper
        """
        try:
            self.database.delete_newspaper(title)
        except Exception:
            raise news_errors.NewsError

    def get_available(self):
        """Get list of registered newspapers with details

        Returns
        -------
             :class:`list`
                A list of dictionaries representing a newspapers with details

        Raises
        -------
            NewsError
                An error occurred when adding newspaper
        """
        try:
            newspapers = self.__get_newspaper__()
            return [{
                'title': newspaper[0],
                'category': newspaper[1],
                'website_url': newspapers[2],
            } for newspaper in newspapers]

        except news_errors:
            raise
        except Exception:
            raise news_errors.NewsError

    def get_categories(self):
        """Get list of registered categories

        Returns
        -------
            :class:`list`
                A list of strings representing all categories.
        Raises
        -------
            NewsError
                An error occurred when adding newspaper
        """
        try:
            return self.database.select_categories()

        except Exception:
            raise news_errors.NewsError

    def get_last_news(self):
        """Get all the news for your registered news feed

        Returns
        -------
             :class:`list`
                A list of dictionaries representing with 5 articles by newspapers registered

        Raises
        -------
            NewsError
                An error occurred when adding newspaper
        """
        try:
            return self.__format_news__(self.__get_newspaper__())

        except news_errors.NewsError:
            raise
        except Exception:
            raise news_errors.NewsError

    def get_news_for_newspaper(self, title):
        """Get last news for a specific newspaper

         Parameters
        -----------
            title: :class:`str`
                Title of the newspaper from where to get news

        Returns
        -------
            :class:`list`
                A list of dictionaries representing 5 articles by newspapers registered

        Raises
        ------
            NewsError
                An error occurred accessing newspapers
        """
        try:
            return self.__format_news__(self.database.select_newspaper_by_title(title))
        except news_errors.NewsError:
            raise
        except Exception:
            raise news_errors.NewsError

    def get_news_for_category(self, category):
        """Get last news for a specific category

         Parameters
        -----------
            category: :class:`str`
                Category name

        Returns
        -------
            :class:`list`
                A list of dictionaries representing 5 articles by newspapers registered

        Raises
        ------
            NewsError
                An error occurred accessing newspapers
        """
        try:
            return self.__format_news__(self.database.select_newspaper_by_cat(category))
        except news_errors.NewsError:
            raise
        except Exception:
            raise news_errors.NewsError

    def __get_newspaper__(self):
        """Get newspapers list from database"""
        newspapers = self.database.select_newspapers()
        if newspapers is None or len(newspapers) <= 0:
            raise news_errors.NoNewspaperFound
        else:
            return newspapers

    def __format_news__(self, raw_newspapers):

        """
        Parameters
        -----------
            raw_newspapers: :class:`list`
                newspaper database result

        Returns
        -------
            :class:`list`
                list: A list of dictionaries representing with 5 articles by newspapers registered

        Raises
        ------
            NewsError
                An error occurred accessing newspapers
        """
        try:
            result = []
            for newspaper in raw_newspapers:
                formatted_newspaper = {
                    'title': newspaper[0],
                    'description': newspaper[1],
                    'website_url': newspaper[2],
                    'articles': []
                }

                rss_result = feedparser.parse(newspaper[3])

                if rss_result is None:
                    raise news_errors.NoArticlesFound

                else:
                    newspaper_articles = rss_result.entries
                    article_count = 0

                    while len(newspaper_articles) > 0 and article_count < self.__NB_ARTICLE_MAX:

                        article = newspaper_articles[article_count]
                        formatted_newspaper['articles'].append({
                            'article_title': article.title,
                            'link': article.link,
                            'date': article.published
                        })
                        article_count += 1

                result.append(formatted_newspaper)

            return result

        except (feedparser.CharacterEncodingUnknown, feedparser.CharacterEncodingOverride,
                feedparser.NonXMLContentType):
            raise news_errors.RssParsingError
        except news_errors.NewsError:
            raise

