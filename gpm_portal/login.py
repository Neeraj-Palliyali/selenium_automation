import load_env as env

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .open_site import open_pages


def login_gpm(driver: WebDriver) -> None:
    driver.get(env.GPM_PORTAL_URL)
    try:
        while True:
            login: WebElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            if login:
                print("------------Login Required------------")
                password: WebElement = driver.find_element(By.ID, 'password')
                submit_show: WebElement = driver.find_element(By.ID, 'submit_show')

                login.send_keys(env.GPM_USERNAME)
                password.send_keys(env.GPM_PASSWORD)
                submit_show.submit()

    except Exception:
        print("------------Logged In------------")

    open_pages(driver=driver)
