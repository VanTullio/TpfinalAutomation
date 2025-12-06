from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_souce'

def get_driver():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)

    time.sleep(5)
   
    return driver


