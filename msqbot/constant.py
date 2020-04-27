import os.path as path

RESOURCE_FOLDER_PATH = path.join(path.dirname(__file__), 'resources')
CONFIG_FILE = path.join(RESOURCE_FOLDER_PATH, 'config.ini')
LOG_FILE = path.join(path.dirname(path.abspath(__file__)), 'logs/')
