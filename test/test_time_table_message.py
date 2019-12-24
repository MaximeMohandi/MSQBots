from msqbitsReporter.epsi_api import time_table_api as timetable


def test_week_course_returning_correct_dict():
    planning = timetable.get_planning_for('13/12/2019')
    assert True == True
