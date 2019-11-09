from datetime import datetime, timedelta


def get_starting_timetable_day():
    """
    Get the date of the first day of the time-table

    This get the current day then compute substract today's
    date with the number of day passed to get the firstday date

    :return: The complete date of the first day of the week or the next week if current day is week-end
    :rtype: datetime
    """
    currentdaystr = datetime.today().strftime("%a").lower()

    # if week-end then start number day at next week first day
    if currentdaystr == 'sat':
        return datetime.today() + timedelta(days=2)
    elif currentdaystr == 'sun':
        return datetime.today() + timedelta(days=1)
    else:
        daytosubs = datetime.today().weekday()
        return datetime.today() - timedelta(days=daytosubs)


def french_to_us_date_converter(frenchdate):
    """
    convert a french date to us date

    :param frenchdate:
    :return us date:
    :rtype: datetime
    """

    dictmonthnumber = [
        ['janvier', '01'], ['février', '02'], ['mars', '03'],
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


def parse_epsi_planning_html(html):
    """
    parse the html of the epsi's school planning into a list of course

    :param html:
    :rtype: html text
    :return table of courses:
    :rtype: table
    """

    weekdays = html.findAll('div', {'class': 'Jour'})  # get the div with the day content in it
    weekcourses = html.findAll('div', {'class': 'Case'})  # get the div with the course information in it
    listweekcourse = []
    cursor = 0

    while cursor < len(weekdays):
        daytitle = weekdays[cursor].td.text
        daycaseLposition = weekdays[cursor]["style"].split(';')[1].split('.')[0].split(':')[1]  # parse the div to get the left position of the day div
        daycourse ={}

        for course in weekcourses:
            coursecasepostion = course["style"].split(';')[3].split('.')[0].split(':')[1]  # parse get the left posiotion of the course div

            if coursecasepostion == daycaseLposition:
                courseinfo = course.findAll('td')
                coursedetails = {}
                temparray= []
                daycourse['day'] = daytitle

                # if the day is the same as the previous course we add new entry in temparray
                if len(listweekcourse) > 0:
                    lastentry = listweekcourse.pop()
                    if lastentry['day'] == daytitle:
                        temparray = lastentry['course']
                    else:
                        listweekcourse.append(lastentry) # pop function destroy the entry, if there's no match we restore it

                for info in courseinfo:
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

