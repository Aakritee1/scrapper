import json
import requests

from bs4 import BeautifulSoup


URL = "http://books.toscrape.com/"
#install git
# create repository n fithub

# go to git bash
#git config --global user.name"Aakritee1"
#git config --global user.email "aakritee88@gmail.com"
#

#git init
#git status => if you want to chech what are the status of the files
#git diff => if you want to check what are the changes
# git add .
#git commit -m "Your Message"
#copy paste git code from github


#git add .       -track files and folders
#git commit -m "Your Message"         -save changes
#git push                        -upload changes to github


def scrape_books(url):
    response = requests.get(url)
    # print(response)
    # print(response.status_code)
    # print(response.text)
    
    if response.status_code !=200:
        print("Failed to fetch the page")
        return
    
    response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = []
    # books = soup.find_all("article", class_="product_pod")
    # for book in books:
    #     title = book.h3.a['title']
    #     price_text = book.find("p", class_="price_color").text
    #     currency = price_text[0]
    #     price = price_text[1:]
        
    #     print(title, currency, price)
    
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        
        books.append({"title": title, "currency": currency, "price": price})

    
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

    print("Data saved to books.json")
    
    
# json bata read garera database ma rakhni
    
    
    
    
    
    
scrape_books(URL)
