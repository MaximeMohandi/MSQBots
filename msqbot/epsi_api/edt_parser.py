from datetime import datetime, timedelta
from . import exception


def clean_start_day():
    """ Get the date of the first day of the time-table

    This get the current day then compute substract today's
    date with the number of day passed to get the firstday date

    Returns
    -------
        :class:`datetime`
            The complete date of the first day of the week or the next week if current day is week-end
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
    """Convert a french date to US date

    Parameters
    -----------
        frenchdate: :class:`str`
            French formated date

    Returns
    -------
        :class:`datetime`
            US formated date

    Raises
    -------
        DateFormatError
            The given date is not in the expected format
    """
    try:
        datetime.strptime(frenchdate, '%d/%m/%y')

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
    except ValueError:
        raise exception.DateFormatError


def parse_epsi_planning_html(html):
    """Parse the html of Beecome.io school planning into a list of course

    Parameters
    -----------
        html: :class:`bs4.BeautifulSoup`
            HTML code of the page.

    Returns
    -------
        :class:`list`
            list of course

    Raises
    -------
    PlanningParsingError
        An occurred when parsing the planning

    """
    planned_courses = []
    cursor = 0

    try:
        day_div = html.findAll('div', {'class': 'Jour'})  # get the div with the day content in it
        course_div = html.findAll('div', {'class': 'Case'})  # get the div with the course information in it

        while cursor < len(day_div):
            day_date = day_div[cursor].td.text
            # get the column position of the day div
            day_case_position = day_div[cursor]["style"].split(';')[1].split('.')[0].split(':')[1]
            day_detail = {}

            for course in course_div:
                # get the position of the course into the planning html table
                course_case_position = course["style"].split(';')[3].split('.')[0].split(':')[1]

                if course_case_position == day_case_position:
                    course_info = course.findAll('td')
                    course_details = {}
                    course_of_day = []
                    day_detail['date'] = day_date

                    # if the day is the same as the previous course we add new entry in course_of_day
                    if len(planned_courses) > 0:
                        last_entry = planned_courses.pop()  # use pop() to get the last entry but it destroy the current entry
                        if last_entry['date'] == day_date:
                            course_of_day = last_entry['course']
                        else:
                            # if there's no match we restore the previously removed entry
                            planned_courses.append(last_entry)

                    # go through the html table class
                    for details in course_info:
                        if details['class'][0] == 'TChdeb':
                            course_details['hours'] = (details.text.split(' - ')[0], details.text.split(' - ')[1])

                        elif details['class'][0] == 'TCase':
                            course_details['label'] = details.text

                        elif details['class'][0] == 'TCProf':
                            course_details['prof'] = details.text.replace('INGENIERIE', '.').split('.')[0]

                        elif details['class'][0] == 'TCSalle':
                            course_details['room'] = details.text

                    course_of_day.append(course_details)
                    day_detail['course'] = course_of_day
                    planned_courses.append(day_detail)
            cursor += 1

        if len(planned_courses) <= 0:
            raise exception.ParserNoPlanningFound
        else:
            return planned_courses

    except (AttributeError, KeyError):
        raise exception.PlanningParsingError

