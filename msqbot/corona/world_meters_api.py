from bs4 import BeautifulSoup
import requests

WORLD_METER_URL = 'https://www.worldometers.info/coronavirus/'


def get_covid_raw_table():
    html = __connect_to_api()
    data = []
    table_body = html.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    return data


def __connect_to_api():
    """
    Connect to worlmeters.info

    :return: worldmeter html page
    """
    request = WORLD_METER_URL
    response = requests.get(request)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('table', {'id': 'main_table_countries_yesterday'})

