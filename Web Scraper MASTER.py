# Web Scraper

# Import libraries
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait




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

# Lable the results
WP_data = [['WP'] + ele for ele in WP_data]







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

# Lable the results
SSE_data = [['SSE'] + [''] + ele for ele in SSE_data]








###--- Northern Power Grid ---###

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

# Lable the results
NPG_data = [['NPG'] + ele for ele in NPG_data]



###--- UK Power Networks ---###

# Define website
UKPN_url = 'http://ukpower.ukpowernetworks.co.uk/power-cut-list'

# Open Safari
safari = webdriver.Chrome()

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

# Lable the results
UKPN_data = [['UKPN'] + ele for ele in UKPN_data]


    

###--- MASTER AFFECTED POSTCODE LIST ---###

# Headers

Headers = [['Supplier Code']+['Loss Time']+['Postcode']+['# Affected']+['Predicted Fix Time']]

# Compile data frames
M_data = Headers + WP_data + SSE_data + NPG_data + UKPN_data

 # Set file type
import csv

# Name the file and write to it
with open("MASTER_Outages.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(M_data)
