import os
import configparser

config = configparser.ConfigParser()
config.read(r'settings.ini')

CHROME_PATH = os.path.join(
    os.path.dirname(__file__),
    "chrome_driver",
    "chromedriver.exe")
USER_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "user_data_selenium", "")

INACESS_URL = config['settings']['INACESS_URL']
INACCESS_USERNAME = config['logins']['INACCESS_USERNAME']
INACCESS_PASSWORD = config['logins']['INACCESS_PASSWORD']
INACCESS_FARMS = config['farms']['INACCESS_PASSWORD_FARMS'].split(',')

GPM_PORTAL_URL = config['settings']['GPM_PORTAL']
GPM_PORTAL_ANALYSIS_URL = config['settings']['GPM_PORTAL_ANALYSIS_URL']
GPM_USERNAME = config['gpm_login']['GPM_USERNAME']
GPM_PASSWORD = config['gpm_login']['GPM_PASSWORD']
GPM_FARMS = config['farms']['GPM_PASSWORD_FARMS'].split(',')
