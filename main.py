import requests
from bs4 import BeautifulSoup

URL = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-1/k0c126l9004?rb=true"
requestPage = requests.get(URL) 
doc = BeautifulSoup(requestPage.text, "html.parser")

numPages = doc.find(class_="pagination")
splitOne = str(numPages).split(">")
splitTwo = str(splitOne).split("</a")[-4]
totalPages = int(str(splitTwo).split("'")[-1])
print(totalPages)

for page in range(1, totalPages + 1):
    URL = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-{page}/k0c126l9004?rb=true"
    requestPage = requests.get(URL) 
    doc = BeautifulSoup(requestPage.text, "html.parser")

    items = doc.find_all(text=re.compile())
