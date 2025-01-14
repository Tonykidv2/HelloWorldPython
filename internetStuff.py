#make sure you pip install request and/BeutifulSoup
#if using Code make sure you are using the correct intepreter most likely the global version

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Extract data from the webpage
data = soup.find('p')
print(data.text)