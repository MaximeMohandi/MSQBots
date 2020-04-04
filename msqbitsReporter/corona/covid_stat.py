from datetime import datetime
import msqbitsReporter.corona.world_meters_api as corona_api


def get_top_10_worst_stat():
    pass


def get_death(country='world'):
    """
    get the number of death by covid-19 for each country

    by default this give world death

    :return: number of death and new death
    """
    full_stat = corona_api.get_covid_raw_table()
    return [{'country': stat[0], 'death': stat[3], 'new_death': stat[4]}
            for stat in full_stat if str.upper(stat[0]) == str.upper(country)][0]


def get_cases(country='world'):
    """
    get the number of known case of covid-19

    by default return the stat for world

    :param country: a country to get stat
    :return: number of known case and new case
    """
    full_stat = corona_api.get_covid_raw_table()
    return [{'country': stat[0], 'cases': stat[1], 'new_cases': stat[2]}
            for stat in full_stat if str.upper(stat[0]) == str.upper(country)][0]


def get_survivors(country='world'):
    """
    get the number of people who survived to covid-19

    :param country: a country to get stat

    :return: number of known survivors
    """
    full_stat = corona_api.get_covid_raw_table()
    return [{'country': stat[0], 'survivors': stat[5]}
            for stat in full_stat if str.upper(stat[0]) == str.upper(country)][0]


def get_french_quarantines_days():
    """
    get the number of quarantines days for french people
    :return: number of quarantines'days
    """
    quarantines_start = datetime(2020, 3, 17)
    return (datetime.now() - quarantines_start).days

