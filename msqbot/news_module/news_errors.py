class NewsError(Exception):
    """News error"""
    pass


class NoArticlesFound(NewsError):
    """No article found for the given RSS feed"""
    pass


class NoNewspaperFound(NewsError):
    """No newspaper found for the request"""
    pass


class RssParsingError(NewsError):
    """A problem occured while pasing the rss feed"""
    pass
