import pytest
import msqbitsReporter.behavior.news_message as news_message


@pytest.mark.parametrize('expected_key', [
    'title',
    'description',
    'footer',
    'articles'
])
def test_get_all_news_success_when_return_expected_dict_key(expected_key):
    fetched_key = news_message.get_all_articles()[0].keys()  # get keys from fetched newspaper articles
    assert expected_key in fetched_key


@pytest.mark.parametrize('dict_key, expected_type', [
    ('title', str),
    ('description', str),
    ('footer', str),
    ('articles', list)
])
def test_get_all_news_success_when_returning_expected_type(dict_key, expected_type):
    fetched_newspapers_keys_type = [type(news[dict_key]) for news in news_message.get_all_articles()]
    assert fetched_newspapers_keys_type.count(expected_type)



def test_getArticlesByNewsPaper_return__a():
    result = news_message.get_all_articles()
    assert len(result) > 0


def test_getAllNewspapersSaved():
    result = news_message.get_saved_newspapers()
    assert len(result) > 0


def test_getAllCategoriesSaved():
    result = news_message.get_saved_categories()
    assert len(result) > 0


# if the method return an empty list
def test_getAllArticlesFromNewspaper():
    result = news_message.get_articles_from(None)
    assert len(result) == 0


def test_get_all_articles_by_cat():
    result = news_message.get_articles_by('TEST')
    assert len(result) > 0
