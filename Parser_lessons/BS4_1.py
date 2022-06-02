from weakref import proxy
from wsgiref import headers
import requests
#proxies = {
#    'https': 'socks5://user:192.252.214.20:15864',
#    'http': 'socks5://user:192.252.214.20:15864'
#}
from bs4 import BeautifulSoup as BS

url = "https://www.avito.ru/"
#url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    
}
req = requests.get(url, headers=headers)
src = req.text
# print(src)


with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)



