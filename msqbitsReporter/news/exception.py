class NewsError(Exception):
    """News error"""
    pass


class NoArticlesFound(NewsError):
    """No article found for the given RSS feed"""
    pass


class NoNewspaperFound(NewsError):
    """No newspaper found for the request"""
    pass


class LocalDatabaseError(NewsError):
    """Something happened during the operation on database"""
    pass


class SavingDatabaseError(LocalDatabaseError):
    """Something happened during the save process"""
    pass


class FetchingDatabaseError(LocalDatabaseError):
    """Something happened when fetching the data"""
    pass


class EmptyArgumentError(NewsError):
    """One or more argument passed is empty"""
    pass


class RssParsingError(NewsError):
    """A problem occured while pasing the rss feed"""
    pass
