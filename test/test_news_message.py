import pytest
import msqbitsReporter.behavior.news_message as newMessage

def test_getArticlesByNewsPaper():
    result = newMessage.getArticlesByNewspaper()
    assert len(result) > 0

def test_getAllNewspapersSaved():
    result = newMessage.getAllNewspapersSaved()
    assert len(result) > 0

def test_getAllCategoriesSaved():
    result = newMessage.getAllCategoriesSaved()
    assert len(result) > 0

def test_getAllArticlesFromNewspaper():
    result = newMessage.getAllArticlesFromNewspaper(None)
    assert len(result) == 0