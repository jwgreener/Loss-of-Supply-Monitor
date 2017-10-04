# Web Scraper

# Import libraries
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Define website
NPG_url = 'http://www.northernpowergrid.com/power-cuts'

# Open Safari
safari = webdriver.Chrome()

safari.get(NPG_url)

time.sleep(5)


html = safari.find_element_by_xpath('//*[@id="tabular"]/div[2]/table')

NPG_html = html.get_attribute('innerHTML')

# Close Safari
safari.quit()

# html parsing
NPG_soup = BeautifulSoup(NPG_html, "html.parser")

NPG_table = NPG_soup



# Define destination array
NPG_data = []

# Find all the rows
NPG_rows = NPG_table.findAll('tr')

# Find all the cols
for NPG_row in NPG_rows:
	NPG_cols = NPG_row.find_all('td')
	NPG_data.append([ele.text.strip() for ele in NPG_cols]) # Append rows and cols into an arrary


# Export the results

# Set file type
import csv

# Name the file and write to it
with open("NPG_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(NPG_data)


    
