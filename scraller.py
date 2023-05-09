#COPY WEBSITE WITH PYTHON
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://google.com'

# Send GET request to the URL
response = requests.get(url)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))

