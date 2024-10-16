from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

#get hold of title and link of the news with most points
soup = BeautifulSoup(response.text, "html.parser")

links_and_titles = soup.select(selector="span.titleline a")
print(links_and_titles[0])