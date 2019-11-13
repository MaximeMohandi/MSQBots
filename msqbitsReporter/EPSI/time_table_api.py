"""
This module is higly depend of the EPSI school planning website. if you want to use it for your own
school planning you can test your function with the test module
"""
import logging
import requests
import msqbitsReporter.EPSI.planing_converter as planning
from bs4 import BeautifulSoup
from datetime import datetime

PLANNING_URI = 'https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel=maxime.mohandi&date={1}'


def get_week_planning():
    try:
        request = PLANNING_URI.format('maxime.mohandi', planning.get_starting_timetable_day())
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")

        return planning.parse_epsi_planning_html(soup)

    except Exception as ex:
        print(ex)
        logging.exception('unable to get week_planning', exc_info=True)


def get_detail_course(date):
    try:
        formateddate = datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
        request = PLANNING_URI.format('maxime.mohandi', formateddate)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        weeksevent =planning.parse_epsi_planning_html(soup)

        for day in weeksevent:
            convertedDate = planning.french_to_us_date_converter(day['day'])
            if convertedDate == formateddate:
                return day

        return 'No event today'

    except Exception as ex:
        print(ex)
        logging.exception('unable to get detailed course', exc_info=True)

def get_detail_course_today():
    try:
        formateddate = datetime.today().strftime('%m/%d/%y')
        request = PLANNING_URI.format('maxime.mohandi', formateddate)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        weeksevent = planning.parse_epsi_planning_html(soup)

        for day in weeksevent:
            convertedDate = planning.french_to_us_date_converter(day['day'])

            if convertedDate == formateddate:
                return day

        return 'No event today'

    except Exception as ex:
        print(ex)
        logging.exception('unable to get detailed course for today', exc_info=True)


def get_next_classroom_today():
    try:
        hournow = datetime.now().hour
        todaycourse = get_detail_course_today()['course']

        if todaycourse is not None:
            for course in todaycourse:
                startHour = int(course['hours'].split('-')[0].split(':')[0])  # parse the result list to get the begining hour
                endHour = int(course['hours'].split('-')[1].split(':')[0].split(' ')[1])   # parse the result list to get the ending hour

                if startHour <= hournow < endHour:
                    return course['room']

        return 'No event today'

    except Exception as ex:
        print(ex)
        logging.exception('unable to get the next classroom', exc_info=True)

