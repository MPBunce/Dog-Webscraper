from bs4 import BeautifulSoup

linkOne = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/k0c126l9004?rb=true"
linkTwo = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-2/k0c126l9004?rb=true"
linkThree = "https://www.kijiji.ca/b-dogs-puppies/ontario/hypoallergenic/page-3/k0c126l9004?rb=true"

requestPage = urlopen(linkOne) 
pageHTML = requestPage.read()
requestPage.close()

html_soup = BeautifulSoup(pageHTML, 'html.parser')