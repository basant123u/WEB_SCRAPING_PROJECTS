""" 
DESCRIPTION:
1. scrape quotes from : http://quotes.toscrape.com
(using beautifulsoup)

2. make three columns for each,
e.g: 
Quote: “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Author: Albert Einstein
Tags: change, deep-thoughts, thinking, world
--------------------------------------------------
Quote: “It is our choices, Harry, that show what we truly are, far more than our abilities.”
Author: J.K. Rowling
Tags: abilities, choices
--------------------------------------------------

3. scrape multiple pages
4. save data to csv or json or excel
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes_final = []
author_final = []
tags_final = []

for t in range(1,11):
# t = int(input())

    url = f"http://quotes.toscrape.com/page/{t}/"

    r = requests.get(url)
    # print(r)
    p = str(r.text)
    # print(p)

    soup = BeautifulSoup(p, "html.parser")

    qt = soup.find_all("span", class_ = "text")
    # print(qt.text)
    # quotes = qt.text
    # print(qt)
    # print(soup.prettify())
    # for quote in quotes:
    #     print(quotes)
    quote_length = len(qt)
    for i in range (quote_length):
        # print(qt[i])
        # print(qt[i].text)
        quotes = quotes_final.append(qt[i].text)
    # print(quotes_final)                           # ******quotes_final*****

    at = soup.find_all("small", class_ = "author")
    # print(at)
    # print(at[1].text)
    author_length = len(at)

    for i in range(author_length):
        # print(at[i].text)
        author = author_final.append(at[i].text)

    # print(author_final)                #******author_final******                         


    tg = soup.find_all("div", class_ = "tags" )
    # print(tg[1].text)
    tag_length = len(tg)
    # print(tag_length)
    for i in range(tag_length):
        tags = tags_final.append(tg[i].text)

    # if t == 9:
    #     # pass
    #     a = "QUOTE : "
    #     b = "-by     "
    #     c = "Tags >> "



    #     for i in range(10):
    #         print(a, quotes_final[i])
    #         print(b, author_final[i])
    #         print(c, tags_final[i])
    #         print()
    #         print("------------------------------------------------------------------------")
    #         print()

        

    # print(tags_final)                 # *****tags_final*****

# quotes_final = []
# author_final = []
# tags_final = []

# Arrange = pd({"Quotes": quotes_final},{"Authors": author_final},{"Tags": tags_final})
# arrange = pd.Arrange()
# print(Arrange)

    # a = "QUOTE : "
    # b = "-by     "
    # c = "Tags >> "



    # for i in range(10):
    #     print(a, quotes_final[i])
    #     print(b, author_final[i])
    #     print(c, tags_final[i])
    #     print()
    #     print("------------------------------------------------------------------------")
    #     print()



# print(quotes_final[0])

final_length = (len(quotes_final))

a = "QUOTE : "
b = "AUTHOR : "
c = "Tags >> "



# for i in range(final_length):
#     print(a, quotes_final[i])
#     print(b, author_final[i])
#     print(c, tags_final[i])
#     print()
#     print("------------------------------------------------------------------------")
#     print()
# print(type(quotes_final))

#ARRANGING AND SAVING TO CSV FILE

# x = pd.DataFrame(quotes_final)
# # print(x)
# y = pd.DataFrame(author_final)
# z = pd.DataFrame(tags_final)

# result = ({"QUOTES":x}, {"AUTHORS":y}, {">>##TAGS##>>"})
# print(result)

data = {"QUOTES": quotes_final, "AUTHORS": author_final}  #">>##TAGS##>>": tags_final }
result = pd.DataFrame(data)
# print(result)
result_final = result.to_csv("quotes.csv")




#tomorrow i will learn it to save =as a file and also scrape more pages and give it to chatGPT...thankyou !!!! 



















