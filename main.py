from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Path to your chromedriver
PATH = r"C:\Users\lucas\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Chrome options
opts = webdriver.ChromeOptions()
opts.add_argument("--user-data-dir=C:\\Users\\lucas\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
opts.add_experimental_option("detach", True)

# Initialize driver
driver = webdriver.Chrome(options=opts)
driver.get("https://tinder.com/app/recs")

# Delay of 30 seconds
time.sleep(15)

body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.ARROW_RIGHT)