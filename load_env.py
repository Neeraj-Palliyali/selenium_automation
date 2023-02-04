import os
from decouple import config

CHROME_PATH = os.path.join(os.path.dirname(__file__), "chrome_driver", "chromedriver.exe")
USER_DATA_PATH = os.path.join(os.path.dirname(__file__), "user_data_selenium", "")

INACESS_URL = config('INACESS_URL')
INACCESS_USERNAME = config('INACCESS_USERNAME')
INACCESS_PASSWORD = config('INACCESS_PASSWORD')