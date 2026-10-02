import requests
from bs4 import BeautifulSoup
import pandas as pd

travel_books = []

url = "https://books.toscrape.com/"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

title = soup.title.text
print(f"Заголовок страницы {title}")

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][-1]
    print(f"Название: {title}, Цена: {price}, Рейтинг: {rating}")

    travel_books.append({
        "Title": title,
        "Price": price,
        "Raring": rating
    })

df = pd.DataFrame(travel_books)

df.to_csv("travel_books.csv", index=False)

print("Данные успешно сохранены в файл books.cvs")

if response.status_code == 200:
    print("Успешно получили страницу!")
else:
    print(f"Ошибка:{response.status_code}")
