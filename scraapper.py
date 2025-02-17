# python -m pip install requests
# get data from web in (HTML,json,xml) format
# python -m pip install beautifulsoup4
# parse html

# install git
# create repository in github

# go to git bash
# git init
# git status
# git diff
# git add .
# git commit -m "Your message"

# 1. code Change
# 2. git add . 
# 3. git commit -m ""
# 4. git push

import requests
from bs4 import BeautifulSoup
import json

URL="https://books.toscrape.com/"

def scrape_books(url):
    response=requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return

    # Set encoding explicitly to handel specail characters
    response.encoding=response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books=soup.find_all("article", class_="product_pod")
    list_data=[]
    for book in books:
        title=book.h3.a["title"]
        price_text=book.find("p", class_="price_color").text
        currency=price_text[0]
        price=price_text[1:]
        dict_data={"Title":title,"Currency":currency,"price":price}
        list_data.append(dict_data)
    return list_data
       
books=scrape_books(URL)
with(open("books.json","w",encoding="utf=8") as f):
    json.dump(books,f,indent=2,ensure_ascii=False)