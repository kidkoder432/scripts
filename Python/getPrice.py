import requests, bs4

def getAmazonPrice(url):
    global price
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    price = elems[0].text.strip()
    return price

price = getAmazonPrice('https://www.amazon.com/gp/product/B00WJ049VU?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=NQMCR3T4HBC8QWVA2MM8')
print(price)





        
