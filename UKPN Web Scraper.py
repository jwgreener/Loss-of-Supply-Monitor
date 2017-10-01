# Web Scraper

# Import libraries
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Define website
UKPN_url = 'http://ukpower.ukpowernetworks.co.uk/power-cut-list'

# Open Safari
safari = webdriver.Safari()

safari.get(UKPN_url)

time.sleep(5)


html = safari.find_element_by_xpath('//*[@id="power-cuts"]/tbody')

UKPN_html = html.get_attribute('innerHTML')

# Close Safari
safari.quit()

# html parsing
UKPN_soup = BeautifulSoup(UKPN_html, "html.parser")

UKPN_table = UKPN_soup



# Define destination array
UKPN_data = []

# Find all the rows
UKPN_rows = UKPN_table.findAll('tr')

# Find all the cols
for UKPN_row in UKPN_rows:
	UKPN_cols = UKPN_row.find_all('td')
	UKPN_data.append([ele.text.strip() for ele in UKPN_cols]) # Append rows and cols into an arrary


# Export the results

# Set file type
import csv

# Name the file and write to it
with open("UKPN_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(UKPN_data)


    
