from platform import platform
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

data = {
    'Name' : [],
    'Platform' : [],
    'Year' : [],
    'Review' : []
}


headers = {'User-Agent': 'Mozilla/5.0'}





# get flatforms 
for p in range(0,193) :
    print(p)
    url = f'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?page={p}'
    html = rq.get(url,headers=headers)
    soup = BeautifulSoup(html.content,'html.parser')

    meta_links = soup.select('a.title > h3')
    list_titles = [x.text for x in meta_links]
    data['Name'].extend(list_titles)

    platforms = soup.find('div',class_='next_to_side_col').findAll('span',class_='data')
    list_paltforms = [x.text.strip() for x in platforms]
    data['Platform'].extend(list_paltforms)

    meta_scores = soup.select('.clamp-score-wrap .metascore_w')
    list_scores = [x.text for x in meta_scores]
    data['Review'].extend(list_scores)

    meta_years = soup.select('.clamp-details > span')
    list_years = [i.text for i in meta_years]
    data['Year'].extend(list_years)


df = pd.DataFrame(data)
df.to_csv('./data/video_games_reviews.csv')
