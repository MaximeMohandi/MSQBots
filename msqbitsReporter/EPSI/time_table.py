import requests
from bs4 import BeautifulSoup
from datetime import date

URL_EPSI_API = 'https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel=maxime.mohandi&date=09/30/2019'

#the api return an HTML document this function split it using the tag representing the needed information
def get_week_planning():
    response = requests.get(URL_EPSI_API)
    soup = BeautifulSoup(response.text, "html.parser")
    weekdays = soup.findAll('div', {'class': 'Jour'})
    weekcourses = soup.findAll('div', {'class': 'Case'})
    listweekcourse = []
    cursor = 0

    while cursor < len(weekdays):
        daytitle = weekdays[cursor].td.text
        daycaseposition = weekdays[cursor]["style"].split(';')[1].split('.')[0].split(':')[1] #get the left posiotion of the day column in the html document
        daycourse ={}
        for course in weekcourses:
            coursecasepostion = course["style"].split(';')[3].split('.')[0].split(':')[1] #get the left posiotion of the course column in the html document
            if coursecasepostion == daycaseposition:

                daycourse['day'] = daytitle
                courseinfo = course.findAll('td')
                coursedetails = {}
                temparray= []

                for info in courseinfo :
                    if info['class'][0] == 'TChdeb':
                        coursedetails['hours'] = info.text
                    elif info['class'][0] == 'TCase':
                        coursedetails['label'] = info.text
                    elif info['class'][0] == 'TCProf':
                        coursedetails['prof'] = info.text.replace('INGENIERIE', '.').split('.')[0]
                    elif info['class'][0] == 'TCSalle':
                        coursedetails['room'] = info.text

                temparray.append(coursedetails)
                daycourse['course'] = temparray
                listweekcourse.append(daycourse)
        cursor += 1
    return listweekcourse

def get_detail_nearest_course():
    pass

