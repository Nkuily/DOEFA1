import requests
from bs4 import BeautifulSoup

url = "https://ctutraining.ac.za/roodepoort-campus/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

imgs = soup.find_all("img")
for img in imgs:
    try:
        name = img['alt']
    except KeyError:
        name = "ImageNoName"+str(imgs.index(img))
    link = img['src']
    with open(name + '.jpg', 'wb') as file:
        down = requests.get('link')
        file.write(down.content)
    print(name, link)
