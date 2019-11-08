import pytest
import msqbitsReporter.behavior.news_message as newMessage

#if the method return a non empty list
def test_getArticlesByNewsPaper():
    result = newMessage.get_all_articles()
    assert len(result) > 0

def test_getAllNewspapersSaved():
    result = newMessage.get_saved_newspapers()
    assert len(result) > 0

def test_getAllCategoriesSaved():
    result = newMessage.get_saved_categories()
    assert len(result) > 0

#if the method return an empty list
def test_getAllArticlesFromNewspaper():
    result = newMessage.get_articles_from(None)
    assert len(result) == 0

def test_get_all_articles_by_cat():
    result = newMessage.get_articles_by('TEST')
    assert len(result) > 0