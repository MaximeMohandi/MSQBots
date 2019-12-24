"""
This module is higly depend of the EPSI school planning website. if you want to use it for your own
school planning you can test your function with the test module
"""
import msqbitsReporter.epsi_api.planning_parser as planning_cleaner
from bs4 import BeautifulSoup
from datetime import datetime
from . import exception
import requests

#TODO inmport common exception to put html error

PLANNING_URI = 'https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel=maxime' \
               '.mohandi&date={} '


def get_week_planning():
    try:
        request = PLANNING_URI.format(planning_cleaner.clean_start_day())
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")

        week_courses = planning_cleaner.parse_epsi_planning_html(soup)
        return __format_courses(week_courses)

    except (requests.ConnectionError, exception.EpsiError):
        raise exception.EpsiError


def get_planning_for(date):
    try:
        given_date = datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
        request = PLANNING_URI.format(given_date)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")

        planned_course_date = planning_cleaner.parse_epsi_planning_html(soup)

        for course in planned_course_date:
            course_date = planning_cleaner.french_to_us_date_converter(course['date'])
            if course_date == given_date:
                return __format_courses([course])  # put course into array to use it with format_courses

    except Exception:
        logging.exception('unable to get detailed course', exc_info=True)


def get_today_planning():
    today_formatted = datetime.today().strftime('%m/%d/%y')
    return get_planning_for(today_formatted)


def get_next_classroom():
    try:
        current_hour = datetime.now().hour
        course_planned_today = get_today_planning()['course']

        if course_planned_today is not None:
            for course in course_planned_today:
                startHour = int(course['hours'].split('-')[0].split(':')[0])  # parse the result list to get the begining hour
                endHour = int(course['hours'].split('-')[1].split(':')[0].split(' ')[1])  # parse the result list to get the ending hour

                if startHour <= current_hour < endHour:
                    return course['room']

    except Exception:
        logging.exception('unable to get the next classroom', exc_info=True)


def __format_courses(planning_details):
    return [{
        'title': planned['date'],
        'courses': [{
            'hourscourse': course['hours'],
            'courselabel': course['label'],
            'courseroom': course['room'],
            'courseteacher': course['prof']
        }for course in planned['course']]
    }for planned in planning_details]