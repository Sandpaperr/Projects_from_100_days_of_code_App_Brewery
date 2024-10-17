from bs4 import BeautifulSoup
import requests

def YCombinator_webiste_scrape(soup: BeautifulSoup):

    links_and_titles_raw = soup.select(selector="span.titleline a")
    score_raw = soup.select(selector="span.score")
    scores = [i.get_text() for i in score_raw]
    print(scores)
    


response = requests.get("https://news.ycombinator.com/news")

#get hold of title and link of the news with most points
soup = BeautifulSoup(response.text, "html.parser")
YCombinator_webiste_scrape(soup)

