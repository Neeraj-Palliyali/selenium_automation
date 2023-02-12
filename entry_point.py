import load_env as env

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from inaccess import login_inaccess
from gpm_portal import login_gpm


if __name__ == '__main__':
    print("------------Starting up------------")

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={env.USER_DATA_PATH}")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options)
    login_gpm(driver=driver)
    login_inaccess(driver=driver)
