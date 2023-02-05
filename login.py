import load_env as env

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def login_inaccess(login: WebElement):
    print("------------Login Required------------")
    password: WebElement = driver.find_element(By.ID, 'password')
    submit_show: WebElement = driver.find_element(By.CLASS_NAME, 'btn')

    login.send_keys(env.INACCESS_USERNAME)
    password.send_keys(env.INACCESS_PASSWORD)
    submit_show.submit()
    print("------------Login Successfull------------")


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


def open_pages(driver: WebDriver):
    print('------------Opening pages------------')
    for plant in env.INACCESS_FARMS:
        element: WebElement = driver.find_element(
            By.XPATH, f"//*[contains(text(), '{plant}')]"
            )

        if element:
            actions = ActionChains(driver)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((
                By.XPATH, f"//*[contains(text(), '{plant}')]"
                )))
            clickable = element.find_element(By.XPATH, "./../../../..")
            driver.execute_script("arguments[0].scrollIntoView();", clickable)
            actions.key_down(Keys.CONTROL) \
                .perform()
            clickable.click()
            actions.key_up(Keys.CONTROL).perform()

    print('------------Pages Opened------------')


if __name__ == '__main__':
    print("------------Starting up------------")

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={env.USER_DATA_PATH}")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options)
    driver.get(env.INACESS_URL)

    try:
        login: WebElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        if login:
            login_inaccess(login)

    except Exception as e:
        print(e)

    set_200_items_per_page(driver=driver)
    open_pages(driver=driver)
