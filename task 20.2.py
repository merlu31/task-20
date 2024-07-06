#selenium python program to downloag photo gallary of given website.
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Setup WebDriver path and options
paths = r"C:\Users\Merlin Archana\chromedriver-win64\chromedriver-win64"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Navigate back to the home page
driver.get("https://labour.gov.in/")
time.sleep(3)

# Navigate to the "Media" menu and then to "Photo Gallery"
media_menu = driver.find_element(By.LINK_TEXT, "Media")
media_menu.click()

allpreseerelease = driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases")
allpreseerelease.click()

photo_gallery_menu = driver.find_element(By.LINK_TEXT, "Photo Gallery")
photo_gallery_menu.click()
time.sleep(5)  # Wait for the page to load

# Create a folder to store the photos
photo_folder = r"C:\Users\Merlin Archana\OneDrive\Desktop\upload\new task\photo gallary"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Download the first 10 photos
photos = driver.find_elements(By.CSS_SELECTOR, "img")[:10]  # Assuming images are <img> elements
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
        file.write(photo_response.content)
    print(f"Downloaded photo {index + 1}")

print("Photos downloaded successfully.")

