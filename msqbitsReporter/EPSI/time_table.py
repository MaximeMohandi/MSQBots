"""
This module is higly depend of the EPSI school planning website. if you want to use it for your own
school planning you can test your function with the test module
"""
import requests
import msqbitsReporter.EPSI.planning as planning
from bs4 import BeautifulSoup
from datetime import datetime

PLANNING_URI = 'http://edtmobilite.wigorservices.net/WebPsDyn.aspx?Action=posETUDSEM&serverid=C&tel=maxime.mohandi&date={1}'

def get_week_planning():
    try:
        request = PLANNING_URI.format('maxime.mohandi',planning.get_first_day_week())
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        return planning.parse_hmtl_result(soup)
    except Exception as ex:
        print(ex)

def get_detail_course(date):
    try:
        formateddate = datetime.strptime(date,'%d/%m/%Y').strftime('%m/%d/%y')
        request = PLANNING_URI.format('maxime.mohandi', formateddate)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        weeksevent =planning.parse_hmtl_result(soup)
        for day in weeksevent:
            convertedDate = planning.convert_full_french_date(day['day'])
            if convertedDate == formateddate:
                return day
        return 'No event today'
    except Exception as ex:
        print(ex)

def get_detail_course_today():
    try:
        formateddate = datetime.today().strftime('%m/%d/%y')
        request = PLANNING_URI.format('maxime.mohandi', formateddate)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        weeksevent = planning.parse_hmtl_result(soup)
        for day in weeksevent:
            convertedDate = planning.convert_full_french_date(day['day'])
            if convertedDate == formateddate:
                return day
        return 'No event today'
    except Exception as ex:
        print(ex)

def get_next_classroom_today():
    try:
        hournow = datetime.now().hour
        todaycourse = get_detail_course_today()['course']
        if todaycourse is not None:
            for course in todaycourse:
                startHour = int(course['hours'].split('-')[0].split(':')[0]) #parse the result list to get the begining hour
                endHour = int(course['hours'].split('-')[1].split(':')[0].split(' ')[1])  #parse the result list to get the ending hour
                if startHour <= hournow < endHour:
                    return course['room']
        return 'No event today'
    except Exception as ex:
        print(ex)
        return 'Probably No event today'
