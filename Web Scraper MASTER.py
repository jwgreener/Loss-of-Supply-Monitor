# Web Scraper

# Import libraries
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup



###--- WESTERN POWER ---###

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
	WP_data.append([ele.text.strip() for ele in WP_cols]) # Append rows and cols into an arrary

# Export the results

# Set file type
import csv

# Name the file and write to it
with open("WP_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(WP_data)


###--- SCOTTISH AND SOUTHERN ELECTRIC ---###

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



 ###--- MASTER AFFECTED POSTCODE LIST ---###

 # Set file type
import csv

# Name the file and write to it
with open("MASTER_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(M_data)