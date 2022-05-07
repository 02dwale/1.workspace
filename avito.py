import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.avito.ru/tomsk/noutbuki?cd=1&q=huawei+matebook+d16")
html = BS(r.content, 'html.parser')


    title = select('.item-price > price')
    print( title[0].text )