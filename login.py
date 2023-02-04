import time
import load_env as env


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def login_inaccess(login :WebElement ):
    print("------------Login Required------------")
    password :WebElement = driver.find_element(By.ID,'password')
    submit_show :WebElement = driver.find_element(By.CLASS_NAME, 'btn')

    login.send_keys(env.INACCESS_USERNAME)
    password.send_keys(env.INACCESS_PASSWORD)   
    time.sleep(4)
    submit_show.submit()
    print("------------Login Successfull------------")


    
if __name__ == '__main__':
    print("------------Starting up------------")
    # chromeOptions  = webdriver.ChromeOptions()
    # chromeOptions .add_argument(f'user-data-dir = /user_data_selenium') 


    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={env.USER_DATA_PATH}") 
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options )
    driver.get(env.INACESS_URL)

    try:
        login :WebElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        if login:
            login_inaccess(login)
    except Exception as e:
        print("jerjer")
        
    