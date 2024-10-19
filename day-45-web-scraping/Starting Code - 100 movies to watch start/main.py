import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Make it a bit more safe, check if response was good first
soup = BeautifulSoup(requests.get(URL).text, "html.parser")

titles = soup.select("h3.title")

with open("./day-45-web-scraping\Starting Code - 100 movies to watch start\movies.txt", "w", encoding="utf-8") as file:
    for title in  reversed(titles):
        title_good = title.get_text()
        file.write(title_good)
        file.write("\n")





