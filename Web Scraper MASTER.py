# Web Scraper

# Import libraries
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup

# Define website
my_url = 'https://www.westernpower.co.uk/Power-outages/Power-cuts-in-your-area/Power-Cut-outages-list.aspx'

# Opening connection, grabbing the webpage
uClient = uReq(my_url)

# Set webpage as variable
html = uClient.read()

# Close connection
uClient.close()

# html parsing
soup = BeautifulSoup(html, "html.parser")

# Grabs power outage table
table = soup.table



rows = table.findAll('tr')

data = []

for row in rows:
	cols = row.find_all('td')
	data.append([ele.text.strip() for ele in cols])


