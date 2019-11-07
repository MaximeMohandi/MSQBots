import pytest
import msqbitsReporter.behavior.news_message as newMessage

#if the method return a non empty list
def test_getArticlesByNewsPaper():
    result = newMessage.getArticlesByNewspaper()
    assert len(result) > 0

def test_getAllNewspapersSaved():
    result = newMessage.getAllNewspapersSaved()
    assert len(result) > 0

def test_getAllCategoriesSaved():
    result = newMessage.getAllCategoriesSaved()
    assert len(result) > 0

#if the method return an empty list
def test_getAllArticlesFromNewspaper():
    result = newMessage.getAllArticlesFromNewspaper(None)
    assert len(result) == 0

def test_get_all_articles_by_cat():
    result = newMessage.getArticlesFromNewspaperBycat('TEST')
    assert len(result) > 0