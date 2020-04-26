class EpsiError(Exception):
    """Something went wrong with the epsi_api module"""
    pass


class DateFormatError(EpsiError):
    """The given date is in the wrong format please check the required date format"""
    pass


class PlanningParsingError(EpsiError):
    """An error occurred during the planning parsing"""
    pass


class ParserNoPlanningFound(EpsiError):
    """The result from the parser has not found any planning for the given date"""
    def __init__(self):
        super().__init__('No Planning has been found')



