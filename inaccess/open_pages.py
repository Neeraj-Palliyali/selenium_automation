import load_env as env

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def open_pages(driver: WebDriver):
    print('------------Opening pages------------')
    for plant in env.INACCESS_FARMS:
        element: WebElement = driver.find_element(
            By.XPATH, f"//*[contains(text(), '{plant}')]")

        if element:
            actions = ActionChains(driver)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((
                By.XPATH, f"//*[contains(text(), '{plant}')]")))
            clickable = element.find_element(By.XPATH, "./../../../..")
            driver.execute_script("arguments[0].scrollIntoView();", clickable)
            actions.key_down(Keys.CONTROL) \
                .perform()
            clickable.click()
            actions.key_up(Keys.CONTROL).perform()

    print('------------Pages Opened------------')
