from msqbitsReporter.EPSI import time_table

def getFormatedPlanningWeek():
    messageStack = []
    allCourse = time_table.get_week_planning()

    for daycourse in allCourse:
        embedcourse = {
            'title': daycourse['day'],
            'courses': []
        }
        for course in daycourse['course']:
            embedcourse['courses'].append({
                'hourscourse': course['hours'],
                'courselabel': course['label'],
                'courseroom': course['room'],
                'courseteacher': course['prof']
            })
        messageStack.append(embedcourse)
    return messageStack

def getPlanningFor(date):
    messageStack = []
    allCourse = time_table.get_detail_course(date)

    if type(allCourse) is not dict:
        embedcourse = {
            'title': allCourse,
            'courses': []
        }
        messageStack.append(embedcourse)
    else:
        embedcourse = {
            'title': allCourse['day'],
            'courses': []
        }
        for course in allCourse['course']:
            embedcourse['courses'].append({
                'hourscourse': course['hours'],
                'courselabel': course['label'],
                'courseroom': course['room'],
                'courseteacher': course['prof']
            })
        messageStack.append(embedcourse)
    return messageStack

def getThePlanningForToday():
    messageStack = []
    allcoursethisday = time_table.get_detail_course_today()

    if type(allcoursethisday) is not dict:
        embedcourse = {
            'title': allcoursethisday,
            'courses': []
        }
        messageStack.append(embedcourse)
    else:
        embedcourse = {
            'title': allcoursethisday['day'],
            'courses': []
        }
        for course in allcoursethisday['course']:
            embedcourse['courses'].append({
                'hourscourse': course['hours'],
                'courselabel': course['label'],
                'courseroom': course['room'],
                'courseteacher': course['prof']
            })
        messageStack.append(embedcourse)
    return messageStack

def getRoomNextClassRoom():
    messageStack = []
    todaycourses = time_table.get_next_classroom_today()
    embedcourse = {
        'title': todaycourses,
        'courses': []
    }
    messageStack.append(embedcourse)
    return messageStack
