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



"""html = rq.get(url,headers=headers)
soup = BeautifulSoup(html.content,'html.parser')"""



# get flatforms 
for p in range(0,100) :
    
    url = f'https://www.metacritic.com/search/game/results?page={p}'
    html = rq.get(url,headers=headers)
    soup = BeautifulSoup(html.content,'html.parser')
    platforms = soup.findAll('span' , {'class' : 'platform'})
    list_paltforms = [x.text for x in platforms]
    data['Platform'].extend(list_paltforms)
    meta_scores = soup.findAll('span' , {'class' : 'metascore_w'})
    list_scores = [x.text for x in meta_scores]
    data['Review'].extend(list_scores)
    meta_links = soup.findAll('h3',{'class':'product_title basic_stat'})
    list_titles = [x.text.strip() for x in meta_links]
    data['Name'].extend(list_titles)
    meta_years = soup.select('.main_stats p')
    list_years = [i.find('span').next_sibling.text.strip() for i in meta_years]
    data['Year'].extend(list_years)
    


df = pd.DataFrame(data)
df.to_csv('./data/video_games_reviews.csv')