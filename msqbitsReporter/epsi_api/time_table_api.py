"""
This module is higly depend of the EPSI school planning website. if you want to use it for your own
school planning you can test your function with the test module
"""
import msqbitsReporter.epsi_api.planning_parser as planning_cleaner
import msqbitsReporter.common.exception as common_error
from . import exception as epsi_error
from bs4 import BeautifulSoup
from datetime import datetime
import requests


PLANNING_URI = 'https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel=maxime' \
               '.mohandi&date={} '


def get_week_planning():
    """
    get the planning for the current week

    :return: list of courses planned this week
    :rtype: list
    """
    try:
        request = PLANNING_URI.format(planning_cleaner.clean_start_day())
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")

        week_courses = planning_cleaner.parse_epsi_planning_html(soup)
        return __format_courses(week_courses)

    except (epsi_error.PlanningParsingError, epsi_error.ParserNoPlanningFound):
        raise

    except requests.ConnectionError:
        raise common_error.HttpError


def get_planning_for(date):
    """
    get the courses planned for the given day

    :return: list of course for the given day
    :rtype: list
    """
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

    except (epsi_error.PlanningParsingError, epsi_error.ParserNoPlanningFound):
        raise

    except requests.ConnectionError:
        raise common_error.HttpError


def get_today_planning():
    """
    return the courses planned for the current day

    :return: list of course planned for the current day
    :rtype: list
    """
    try:
        today_formatted = datetime.today().strftime('%m/%d/%y')
        return get_planning_for(today_formatted)

    except (epsi_error.PlanningParsingError, epsi_error.ParserNoPlanningFound, common_error.HttpError):
        raise


def get_next_classroom():
    """
    get the classroom number for the next course of the current day

    :return: next classroom number
    :rtype: dict
    """
    try:
        current_hour = datetime.now().hour
        course_planned_today = get_today_planning()['course']

        if course_planned_today is not None:
            for course in course_planned_today:
                startHour = int(course['hours'].split('-')[0].split(':')[0])  # parse the result list to get the begining hour
                endHour = int(course['hours'].split('-')[1].split(':')[0].split(' ')[1])  # parse the result list to get the ending hour

                if startHour <= current_hour < endHour:
                    return course['room']

    except (epsi_error.PlanningParsingError, epsi_error.ParserNoPlanningFound, common_error.HttpError):
        raise


def __format_courses(planning_details):
    """
    format the html parsed result into a comprehensible list of courses

    :return:  list of dictionary with date and courses
    :rtype: list
    """
    return [{
        'title': planned['date'],
        'courses': [{
            'hourscourse': course['hours'],
            'courselabel': course['label'],
            'courseroom': course['room'],
            'courseteacher': course['prof']
        }for course in planned['course']]
    }for planned in planning_details]
