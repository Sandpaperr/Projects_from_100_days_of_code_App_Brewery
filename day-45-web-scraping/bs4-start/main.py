from bs4 import BeautifulSoup
import requests

def YCombinator_webiste_scrape(soup: BeautifulSoup):

    links_and_titles_raw =[i.find(name="a") for i in soup.select(selector="span.titleline")] 
    links = [i.get("href") for i in links_and_titles_raw]
    titles = [i.get_text() for i in links_and_titles_raw]

    # every title has a subtext
    sublines = [i for i in soup.select(selector="td.subtext")]
    scores = []
    
    for raw in sublines:
        #only the titles that have score has a subline
        subline = raw.find(name="span", class_="subline")

        if subline is None:
            scores.append(0)
        else:
            scores.append(int(subline.find(name="span", class_="score").get_text().split()[0]))


    dict_for_scores_titles_links = {}

    for i in range(len(scores)):
        dict_for_scores_titles_links[scores[i]] = [titles[i], links[i]]


    max_score = max(dict_for_scores_titles_links)
    print(max_score , dict_for_scores_titles_links[max_score])

    
    
    

    


response = requests.get("https://news.ycombinator.com/news")

#get hold of title and link of the news with most points
soup = BeautifulSoup(response.text, "html.parser")
YCombinator_webiste_scrape(soup)

