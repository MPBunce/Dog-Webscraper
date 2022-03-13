import requests
from bs4 import BeautifulSoup

URL = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-1/k0c126l9004?rb=true""

requestPage = requests.get(URL) 
pageHTML = requestPage.read()
requestPage.close()

html_soup = BeautifulSoup(pageHTML, 'html.parser')