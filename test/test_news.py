from msqbitsReporter.news import news_local_db as news, exception as ex
import sqlite3
import pytest

TEST_RSS_LINK = 'http://feeds.feedburner.com/TechCrunch/'  # is used to avoid error from feedparser


def test_insert_newspaper_success():
    db = news.LocalDatabase('test_database.db')
    id = db.insert_newspaper('test', 'test', 'test', 'IT')
    assert(type(id) is int)


def test_insert_newspaper_TypeError_when_not_enough_argument():
    db = news.LocalDatabase('test_database.db')
    with pytest.raises(TypeError):
        db.insert_newspaper('test', 2, dict)


def test_insert_newspaper_SavingDatabaseError_when_wrong_category():
    db = news.LocalDatabase('test_database.db')
    with pytest.raises(ex.SavingDatabaseError):
        db.insert_newspaper('test', 'test', 'test', -1)


@pytest.mark.parametrize('wrong_input',
                         [(dict, 'good_lin', 'good_rss', 'IT'),
                          ('good_title', 'good_link', list, 'Transport'),
                          ('good_title', 'good_link', 'good_rss', 'FAKE')])
def test_insert_newspaper_SavingDatabaseError_when_wrong_argument_type(wrong_input):
    db = news.LocalDatabase('test_database.db')
    with pytest.raises(ex.SavingDatabaseError):
        db.insert_newspaper(wrong_input[0], wrong_input[1], wrong_input[2], wrong_input[3])


def test_delete_newspaper_success():
    db = news.LocalDatabase('test_database.db')
    db.insert_newspaper('to_delete', 'to_delete_site', TEST_RSS_LINK, 'IT')
    db.delete_newspaper('to_delete')


def test_select_newspaper_return_not_null():
    db = news.LocalDatabase('test_database.db')
    db.insert_newspaper('to_delete', 'to_delete_site', TEST_RSS_LINK, 'IT')
    assert (db.select_newspapers() is not None)
    db.delete_newspaper('to_delete')


def test_select_newspaper_return_correct_dict():
    pass
