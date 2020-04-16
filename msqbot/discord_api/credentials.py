import configparser
import logging
import common.constant as const


def get_credentials(section):
    try:
        config = configparser.ConfigParser()
        config.read(const.CONFIG_FILE)
        return config[section.upper()]
    except configparser.Error as error:
        print(f'error getting credentials for {section} : {error.message}')
        logging.exception('unable to get credentials', exc_info=True)
