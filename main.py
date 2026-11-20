import csv
import time
import requests
from bs4 import BeautifulSoup

all_books = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        all_books.append([title, price])

    print("Page", page, "done -", len(books), "books")
    time.sleep(0.5)

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(all_books)

print("Saved", len(all_books), "books to books.csv")