from datetime import date
import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://vk.com/im?sel=c69")
html = BS(r.content, 'html.parser')

title = html.title
print("\n", title.text, "\n")
    

#raspisanie = html.find("div", class_ = "table-responsive").find_all("span", class_="discipline")
#print(raspisanie.text)
