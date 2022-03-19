import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-1/k0c126l9004?rb=true"
requestPage = requests.get(URL) 
doc = BeautifulSoup(requestPage.text, "html.parser")

numPages = doc.find(class_="pagination")
splitOne = str(numPages).split(">")
splitTwo = str(splitOne).split("</a")[-4]
totalPages = int(str(splitTwo).split("'")[-1])
print(totalPages)

partOneUrl = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-"
partTwoUrl = "/k0c126l9004?rb=true"


for page in range(1, totalPages + 1):

    num = str(page)
    print(num)
    url = partOneUrl+num+partTwoUrl
    print(url)
    requestPage = requests.get(url) 
    doc = BeautifulSoup(requestPage.text, "html.parser")
    testPageNumber = doc.find(class_="pagination")
    print(testPageNumber)
  
