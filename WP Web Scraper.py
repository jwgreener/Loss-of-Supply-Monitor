# Web Scraper

# Import libraries
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup

# Define website
WP_url = 'https://www.westernpower.co.uk/Power-outages/Power-cuts-in-your-area/Power-Cut-outages-list.aspx'

# Opening connection, grabbing the webpage
uClient = uReq(WP_url)

# Set webpage as variable
WP_html = uClient.read()

# Close connection
uClient.close()

# html parsing
WP_soup = BeautifulSoup(WP_html, "html.parser")

# Grabs power outage table
WP_table = WP_soup.table

# Find all the rows
WP_rows = WP_table.findAll('tr')

# Define destination array
WP_data = []


# Find all the cols
for WP_row in WP_rows:
	WP_cols = WP_row.find_all('td')
	WP_data.append([ele.text.strip() for ele in WP_cols]) # Append rows and cols into an arrary <----------


# Export the results

# Set file type
import csv

# Name the file and write to it
with open("WP_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(WP_data)

    #headers = row[0]

	#data = row[1:]

    
