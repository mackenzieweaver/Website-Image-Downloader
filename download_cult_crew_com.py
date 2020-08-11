import requests
import bs4
import os

res = requests.get('https://cultcrew.com/')
playFile = open('cultcrew.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
cultcrewSoup = bs4.BeautifulSoup(res.text, "html.parser")
elements = cultcrewSoup.find_all('img')

for i in elements:
    try:
        url = 'http:' + i.attrs['src']
        name = os.path.basename(url).split('?')
        print('Downloading %s' % name[0])
        res = requests.get(url)
        res.raise_for_status()
        imageFile = open(name[0], 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    except:
        print('no src')
