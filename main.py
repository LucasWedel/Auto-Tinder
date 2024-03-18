from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import re
import random




# Function to simulate space search and scrape images
def space_search_and_scrape(driver):
    # Send space bar to perform space search
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)
    time.sleep(random.uniform(1, 4))  # Add a short delay for the next image to load
    
    # Find and scrape all div elements with background image URLs
    elements = driver.find_elements(By.CSS_SELECTOR, '[style*="background-image"][style*="gotinder.com/u/"]')
    
    # Extract URLs from style attribute
    scraped_urls = []
    for element in elements:
        # Get the style attribute value
        style_attribute = element.get_attribute("style")
        # Extract URL using string manipulation
        url_start_index = style_attribute.find('url("') + len('url("')
        url_end_index = style_attribute.find('")', url_start_index)
        if url_start_index != -1 and url_end_index != -1:
            url = style_attribute[url_start_index:url_end_index]
            scraped_urls.append(url)
        else:
            print("URL not found for element:", element.get_attribute("outerHTML"))
            
    return scraped_urls



# Path to your chromedriver
PATH = r"C:\Users\lucas\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Chrome options
opts = webdriver.ChromeOptions()
opts.add_argument("--user-data-dir=C:\\Users\\lucas\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
opts.add_experimental_option("detach", True)

# Initialize driver-
driver = webdriver.Chrome(options=opts)
driver.get("https://tinder.com/app/recs")


for j in range(200):
    time.sleep(random.uniform(7, 13))
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.bullet[aria-label*="1 af"][aria-label*="tilgængelige billeder"]')

    # Check if there are buttons found
    if buttons and len(buttons) > 1:
        # Get the second button
        button = buttons[1]
        
        # Extract the value of X from the aria-label attribute
        aria_label = button.get_attribute("aria-label")
        if aria_label:
            parts = aria_label.split(" ")
            if "af" in parts and "tilgængelige" in parts:
                x_index = parts.index("tilgængelige") - 1
                if x_index >= 0:
                    total_images = parts[x_index]
                    print("Total available images:", total_images)
                else:
                    print("Could not determine the total number of available images.")
            else:
                print("Could not find the relevant parts in the aria-label attribute.")
        else:
            print("aria-label attribute not found for the button.")
    else:
        print("Second button with the specified description not found.")
        
        
    total_images = int(total_images)
    # Track the number of space searches needed
    space_search_count = [0] * total_images

    # Initialize an empty set to store unique URLs
    unique_urls = set()

    for i in range(total_images):
        # Perform space search and scrape images
        scraped_urls = space_search_and_scrape(driver)
        
        # Add scraped URLs to the set of unique URLs
        unique_urls.update(scraped_urls[1:])
        
        # Update space search count for the next step
        if i < total_images - 1:
            space_search_count[i+1] += 1
            
    # Find all div elements
    elements = driver.find_elements(By.TAG_NAME, 'div')

    # Find all elements with a partial match of background image URL in the style attribute
    elements = driver.find_elements(By.CSS_SELECTOR, '[style*="background-image"][style*="gotinder.com/u/"]')

    # Find the span element and extract the name
    name_elements = driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="name"]')
    name = name_elements[1].text
    
    # Find all span elements and extract the second age
    age_elements = driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="age"]')
    age = age_elements[1].text

    # Define the separator
    separator = "\n----------------\n"

    # Join the URLs with the separator and print
    print("Unique URLs:", separator.join(unique_urls))

    # Read the existing URLs from the file
    with open('urls.txt', 'r') as f:
        existing_urls = set(line.strip() for line in f)

    # Remove any URLs that are already in the file from unique_urls
    unique_urls -= existing_urls

    # If there are any new unique URLs, write them to the file
    if unique_urls:
        # Join the URLs with the separator
        url_string = separator.join(unique_urls)
        url_string += "\n----------------\n"
        url_string = f"Navn: {name}\nAlder: {age}\n" + url_string
        # Open the file in append mode
        with open('urls.txt', 'a') as f:
            # Write the URL string to the file
            f.write(url_string)
        
    driver.refresh()


#body = driver.find_element(By.TAG_NAME, 'body')
#body.send_keys(Keys.ARROW_RIGHT)