from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def set_200_items_per_page(driver: WebDriver):
    print('------------Starting dropdown------------')
    items_per_page: WebElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'uds-btn-icon-clear'))
    )
    driver.execute_script("arguments[0].click();", items_per_page)

    dropdown_xpath = '''//*[@id="NG2_UPGRADE_26_0"]/div/div[2]/pagination/div/
    div[1]/div[3]/fang-dropdown/div/div/div[2]/div/div[4]/p'''

    item_200: WebElement = driver.find_element(By.XPATH, dropdown_xpath)
    driver.execute_script("arguments[0].click();", item_200)

    print('------------Dropdown Selected------------')
