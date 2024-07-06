#selenium python program to download monthly progress report of given website.
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

# Open the Labour Ministry website
driver.get("https://labour.gov.in/")
time.sleep(3)

# Navigate to the "Documents" menu
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(2)  # Wait for the dropdown menu to appear

# Click on "Monthly Progress Report"
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute('href')

# Download the monthly progress report
report_response = requests.get(monthly_report_url)
with open(r"C:\Users\Merlin Archana\OneDrive\Desktop\upload\new task\monthly progress report.docx", 'wb') as file:
    file.write(report_response.content)

print("Monthly Progress Report downloaded successfully.")

