import load_env as env

import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def open_pages(driver: WebDriver) -> None:
    print('------------Opening pages------------')
    index = 0
    for plant in env.GPM_FARMS:
        driver.execute_script(f"window.open('{env.GPM_PORTAL_URL}')")
        index += 1
        driver.switch_to.window(driver.window_handles[index])
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'name')))
            element: WebElement = driver.find_element(
                By.XPATH, f"//a[contains(text(), '{plant}')]")

            if element:
                plant_id = element.get_attribute('href').split('/')[-1]
                driver.get(env.GPM_PORTAL_ANALYSIS_URL + plant_id)

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//option[contains(text(), 'Inverter')]")))
                inverter_option = driver.find_element(
                    By.XPATH, "//option[contains(text(), 'Inverter')]"
                )
                inverter_option.click()

                time.sleep(1)
                check_boxs = driver.find_elements(
                    By.XPATH, "//span[contains(text(), 'Elements')]")

                for check_box in check_boxs:
                    if check_box.size['height'] > 0 and check_box.size['width'] > 0:
                        check_box.click()

                time.sleep(1)
                options = ['AC POWER', 'ACTIVE POWER']
                for option in options:
                    try:
                        power_option = driver.find_element(
                            By.XPATH, f"//span[contains(text(), '{option}')]"
                        )
                        power_option.click()
                        break
                    except Exception:
                        continue
                time.sleep(1)
                ok_buttons = driver.find_elements(
                    By.XPATH, "//button[contains(text(), 'Ok')]")

                for ok_button in ok_buttons:
                    if ok_button.size['height'] > 0 and ok_button.size['width'] > 0:
                        ok_button.click()

                all_day = driver.find_element(By.XPATH, "//button[contains(text(), 'All day')]")
                all_day.click()

                chart = driver.find_element(By.XPATH, "//a[contains(text(), 'Chart')]")
                chart.click()

        except Exception:
            logging.debug(f"ERROR on id: {plant_id}")

    driver.switch_to.window(driver.window_handles[0])
    print('------------Pages Opened------------')
