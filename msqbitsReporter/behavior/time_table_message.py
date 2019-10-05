from msqbitsReporter.EPSI import time_table

def getPlanningWeek():
    messageStack = []
    allCourse = time_table.get_week_planning()

    for workedday in allCourse:
        messageStack.append(
            """🗓️ **{0}**""".format(workedday['day'])
        )
        for course in workedday['course']:
            messageStack.append(
                """**{0} - {1} :**\n {2}\n -  {3}\n"""
                .format(course['hours'], course['label'], course['room'], course['prof'])
            )
    return messageStack

def getPlanningFor(date):
    messageStack = []
    allCourse = time_table.get_detail_course(date)

    if type(allCourse) is not dict:
        messageStack.append(allCourse)
    else:
        messageStack.append(
            """🗓️ **{0}**""".format(allCourse['day'])
        )
        for course in allCourse['course']:
            messageStack.append(
                """**{0} - {1} :**\n {2}\n -  {3}\n"""
                .format(course['hours'], course['label'], course['room'], course['prof'])
            )
    return messageStack

def getThePlanningForToday():
    messageStack = []
    allcoursethisday = time_table.get_detail_course_today()

    if type(allcoursethisday) is not dict:
        messageStack.append(allcoursethisday)
    else:
        messageStack.append(
            """🗓️ **{0}**""".format(allcoursethisday['day'])
        )
        for course in allcoursethisday['course']:
            messageStack.append(
                """**{0} - {1} :**\n {2}\n -  {3}\n"""
                    .format(course['hours'], course['label'], course['room'], course['prof'])
            )
    return messageStack

def getRoomNextClassRoom():
    messageStack = []
    todaycourses = time_table.get_next_classroom_today()

    if type(todaycourses) is not dict:
        messageStack.append(todaycourses)
    else:
        messageStack.append(
            """next classroom : {0}""".format(todaycourses)
        )
    return messageStack
