"""
1. scraping url = https://books.toscrape.com/

2. Data :
Title — the full name of the book

Price — shown in pounds (e.g., “£51.77”)

Availability — whether it’s in stock or not

Rating — star rating (given as words like “One”, “Two”, “Five”)

3. all 50 pages

4. convert into csv, json, xlsx

5. EG: 

TITLE	PRICE	AVAILABILITY	RATING
A Light in the Attic	£51.77	In stock	Three
Tipping the Velvet	£53.74	In stock	One
...	...	...	...
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

title = []
price = []
availability = []
rating = []

for pageno in range(1,51):
    
    url = f"https://books.toscrape.com/catalogue/page-{pageno}.html"

    r = requests.get(url)
    # print(r)
    p = str(r.text)
    # print(p)

    soup = BeautifulSoup(p, "html.parser")

    # title = soup.find("a", href="")
    # print(title)

    for i in soup("a"):
        x = i.get("title")
        if x == None:
            continue
        else:
            # print(x)
            title_app = title.append(x)
    # print(title)                               #>>>title


    prc = soup.find_all("p", class_ = "price_color")
    # print(prc)
    price_length = len(prc)
    for i in range (price_length): 
        s = str(prc[i].text)
        l = len(s)
        # print(s[1:l])
        price_demo = s[1:l]
        price_app = price.append(price_demo)

    # print(price)                               #>>>price

    ava = soup.find_all("p", class_ = "instock availability")

    # print(len(ava.text))
    # s = str(ava.text)
    # l = len(s)
    # ava_demo = s[15:23]
    # print(ava_demo)

    ava_length = len(ava)
    # print(ava_length)
    for i in range(ava_length):
        s = str(ava[i].text)
        ava_demo = s[15:23]
        # print(ava_demo)
        # print(ava[i].text)
        # print(len(ava[i].text))
        ava_append = availability.append(ava_demo)

    # print(availability)                        #>>>availability
    # print(len(availability)) 

    # at_list =("One","Two","Three","Four","Five")
    # rat = soup.find_all("p", class_ =f"star-rating {at_list[0]}")
    # # print(rat)
    # print(len(rat))

    # rat = soup.find("article", class_ = "product_pod")
    # print(rat)

    for i in soup("p"):
        x = i.get("class")
        # print(x)
        if x == ["price_color"]:
            continue
        if x == ["instock", "availability"]:
            continue
        else:
            # print(x[1])
            rat_append = rating.append(x[1])

    # print(rating)                     #>>>>>rating

# print(len(title))
# print(len(price))
# print(len(availability))
# print(len(rating))

#SAVING TO CSV FILE

data = {"TITLE": title, "PRICE": price, "AVAILABILITY": availability, "RATING": rating}
df = pd.DataFrame(data)

df_final = df.to_csv("books.csv")











