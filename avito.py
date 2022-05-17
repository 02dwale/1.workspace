import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.avito.ru/rossiya/noutbuki?cd=1&q=huawei+matebook+d16")
html = BS(r.content, 'html.parser')

for el in html.select(".items-items-kAJAg > .iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"):
    title = el.select('.price-price-JP7qe > .price-text-_YGDY text-text-LurtD text-size-s-BxGpL')
    print( title[0].text )
    
    
    