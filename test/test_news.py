from msqbitsReporter.news import news_local_db as news, exception as ex
import sqlite3
import pytest


def test_insert_newspaper_success():
    db = news.LocalDatabase('test_database.db')
    db.insert_newspaper('test', 'test', 'test', 'IT')


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
    pass


def test_delete_newspaper_no_enough_argument():
    pass


def test_select_newspaper_return_correct_dict():
    pass
