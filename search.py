import requests
from bs4 import BeautifulSoup as bs

url = 'https://vc.ru'


def getNews():
    try:
        r = requests.get(url)
        webpage = bs(r.content)
        #for title in webpage.select('div.content-container div.content-title--short')[0]:
           # print(title.text)
        for news in webpage.select('div.l-island-a p')[0]:
            return news

    except Exception as e:
        return "Sorry I can't found"



getNews()




