import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-1/k0c126l9004?rb=true"
requestPage = requests.get(URL) 
doc = BeautifulSoup(requestPage.text, "html.parser")

numPages = doc.find(class_="pagination")
splitOne = str(numPages).split(">")
splitTwo = str(splitOne).split("</a")[-4]
totalPages = int(str(splitTwo).split("'")[-1])
print("The total number of pages is: "+ str(totalPages))

partOneUrl = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-"
partTwoUrl = "/k0c126l9004?rb=true"

data = []

for page in range(1, totalPages + 1):

    num = str(page)
    print("The number of iterations is " + str(num))
    
    url = partOneUrl+num+partTwoUrl

    requestPage = requests.get(url) 
    doc = BeautifulSoup(requestPage.text, "html.parser")

    # info container
    info_container = doc.find_all(class_="info-container")
    for ad in info_container:
        dogPrice = ad.find(class_="price").get_text().strip()
        dogTitle = ad.find(class_="title").get_text().strip()
        dogLink = 'kijiji.ca'+ ad.find('a').get('href')
        data.append([dogTitle,dogPrice,dogLink])
        
df=pd.DataFrame(data, columns=['Title', 'Price', 'Link'])

df.to_csv('dogDict.csv')
print('csv Exported')
