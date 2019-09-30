from datetime import datetime, timedelta


def get_first_day_week() :
    numbertoday = datetime.today().weekday()
    return datetime.today() - timedelta(days=numbertoday)

def convert_full_french_date(frenchdate):
    dictmonthnumber = [
        ['janvier', '01'], ['fevrier', '02'], ['mars', '03'],
        ['avril', '04'], ['mai', '05'], ['juin', '06'],
        ['juillet', '07'], ['aout', '08'], ['septembre', '09'],
        ['octobre', '10'], ['novembre', '11'], ['décembre', '12']
    ]
    correctdate = frenchdate.split(' ')

    for date in dictmonthnumber:
        if correctdate[2].lower() == date[0]:
            yeardate = datetime.today().year
            dateday = correctdate[1]
            datemonth = date[1]

            return datetime(year=int(yeardate), month=int(datemonth), day=int(dateday)).strftime('%m/%d/%y')

def parse_hmtl_result(parsedhtml):
    weekdays = parsedhtml.findAll('div', {'class': 'Jour'})
    weekcourses = parsedhtml.findAll('div', {'class': 'Case'})
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