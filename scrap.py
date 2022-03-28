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
url = 'https://www.metacritic.com/search/game/results'


html = rq.get(url,headers=headers)
soup = BeautifulSoup(html.content,'html.parser')

# store  html file 
with open('test.html','w', encoding="utf-8") as file :
    file.write(html.text)

# get flatforms 
platforms = soup.findAll('span' , {'class' : 'platform'})
list_paltforms = [x.text for x in platforms]
data['Platform'] = list_paltforms

# get review
meta_scores = soup.findAll('span' , {'class' : 'metascore_w'})
list_scores = [x.text for x in meta_scores]
data['Review'] = list_scores


# get links

meta_links = soup.findAll('h3',{'class':'product_title basic_stat'})
list_titles = [x.text.strip() for x in meta_links]
data['Name'] = list_titles


meta_years = soup.select('.main_stats p')

list_years = [i.find('span').next_sibling.text.strip() for i in meta_years]

data['Year'] = list_years

df = pd.DataFrame(data)
df.to_csv('video_games_review.csv')
# list_years = [i.text.strip() for i in meta_years]

# list_years = [x.text.strip() for x in meta_years]

