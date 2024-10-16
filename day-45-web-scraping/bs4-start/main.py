from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
print(response.text)
#get hold of title and link of the news with most points
soup = BeautifulSoup(response.text, "html.parser")

links_and_titles = soup.find_all(name="a")