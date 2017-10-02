# Web Scraper

# Import libraries
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup

# Define website
SSE_url = 'https://www.ssepd.co.uk/Powertrack/'

# Opening connection, grabbing the webpage
uClient = uReq(SSE_url)

# Set webpage as variable
SSE_html = uClient.read()

# Close connection
uClient.close()

# html parsing
SSE_soup = BeautifulSoup(SSE_html, "html.parser")

# Find all the postcode rows
SSE_rows = SSE_soup.findAll("div", { "class" : "col-xs-12 col-sm-3 col-md-2" } )

# Define destination array
SSE_data = []

# Extract postcodes
for ele in SSE_rows:
	SSE_data.append([ele.text.strip()])

# Export the results

# Set file type
import csv

# Name the file and write to it
with open("SSE_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(SSE_data)