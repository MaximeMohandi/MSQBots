"""
This module is higly depend of the EPSI school planning website. if you want to use it for your own
school planning you can test your function with the test module
"""
import requests
import msqbitsReporter.EPSI.planning as planning
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

PLANNING_URI = 'https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel={0}&date={1}'

def get_week_planning():
    try:
        request = PLANNING_URI.format('maxime.mohandi',planning.get_first_day_week())
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        return planning.parse_hmtl_result(soup)
    except Exception as ex:
        print(ex)

def get_detail_nearest_course(date):
    try:
        formateddate = datetime.strptime(date,'%d/%m/%Y').strftime('%m/%d/%y')
        request = PLANNING_URI.format('maxime.mohandi', formateddate)
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")
        weeksevent =planning.parse_hmtl_result(soup)
        for day in weeksevent:
            if planning.convert_full_french_date(day['day']) == formateddate:
                return day
        return 'No event today'
    except Exception as ex:
        print(ex)



print(get_detail_nearest_course('02/10/2019'))