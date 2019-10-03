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
                """⏰ {0}\n 📓 {1}\n 👨‍🏫 {2}\n 🚪 {3}\n"""
                .format(course['hours'], course['label'], course['prof'], course['room'])
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
                """⏰ {0}\n 📓 {1}\n 👨‍🏫 {2}\n 🚪 {3}\n"""
                    .format(course['hours'], course['label'], course['prof'], course['room'])
        )
    return messageStack
