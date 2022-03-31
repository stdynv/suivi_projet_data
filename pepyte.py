import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd


data = {
        'Nom Ecole' : [],
        'Niveau' : [],
        'Type' : [],
        'Tel' : [],
        'Email' : []
    }
# function to return text element 
def get_text(element):
    col = []
    for i in element:
        col.append(i.text.strip())
    return col

# A function that scrap all elements of a page 
def page_df(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    parent_div = soup.select(".post-block")
    for child in parent_div : 
        
        nom_etab = child.select_one('.establishment--search_item__content > h2')
        data['Nom Ecole'].extend(get_text(nom_etab)) if nom_etab else data['Nom Ecole'].append('Not Found')
        
        niveau = child.find("span", {"class": "establishment-high-school establishment-type"})
        data['Niveau'].extend(get_text(niveau)) if niveau else data['Niveau'].append('Not Found')
        
        type_etab = child.select_one('.establishment-public')
        data['Type'].extend(get_text(type_etab)) if type_etab else data['Type'].append('Not Found')
        
        tel_etab = child.select_one('.establishment--search_item__contact > a')
        data['Tel'].append(tel_etab['href'][4:]) if tel_etab else data['Tel'].append('Not Found')

        email_etab = child.select_one('.establishment--search_item__address > p:last-child > a')
        data['Email'].append(email_etab.text) if email_etab else data['Email'].append('Not Found')

        
# scrap 30 pages
for p in range(0,30) :
    url = f'https://www.education.gouv.fr/annuaire?keywords=&department=&academy=1&status=All&establishment=All&geo_point=&page={p}'
    page_df(url)
    
df = pd.DataFrame(data)
df.to_csv('liste_des_ecoles.csv')