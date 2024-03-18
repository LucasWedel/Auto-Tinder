from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import re

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
time.sleep(7)

for i in range(0, 10):
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)
    time.sleep(1)


# Find all elements with background image URL starting with the specified pattern
# Find all div elements
elements = driver.find_elements(By.TAG_NAME, 'div')

# Find all elements with a partial match of background image URL in the style attribute
elements = driver.find_elements(By.CSS_SELECTOR, '[style*="background-image"][style*="gotinder.com/u/"]')

# Print the number of elements found
print("Number of elements found:", len(elements))

for element in elements:
    # Get the style attribute value
    style_attribute = element.get_attribute("style")
    # Extract URL using string manipulation
    url_start_index = style_attribute.find('url("') + len('url("')
    url_end_index = style_attribute.find('")', url_start_index)
    if url_start_index != -1 and url_end_index != -1:
        url = style_attribute[url_start_index:url_end_index]
        print(url)
    else:
        print("URL not found for element:", element.get_attribute("outerHTML"))


#body = driver.find_element(By.TAG_NAME, 'body')
#body.send_keys(Keys.ARROW_RIGHT)