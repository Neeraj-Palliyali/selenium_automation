import load_env as env

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .open_pages import open_pages
from .set_200_pages import set_200_items_per_page


def login_inaccess(driver: WebDriver) -> None:
    driver.get(env.INACESS_URL)

    try:
        login: WebElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        if login:
            print("------------Login Required------------")
            password: WebElement = driver.find_element(By.ID, 'password')
            submit_show: WebElement = driver.find_element(By.CLASS_NAME, 'btn')

            login.send_keys(env.INACCESS_USERNAME)
            password.send_keys(env.INACCESS_PASSWORD)
            submit_show.submit()
            print("------------Login Successfull------------")

    except Exception:
        print("------------Logged In------------")

    set_200_items_per_page(driver=driver)
    open_pages(driver=driver)
