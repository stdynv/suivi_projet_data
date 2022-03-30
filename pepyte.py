from click import get_text_stream
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd


data = {
        'Nom Ecole' : [],
        'Niveau' : [],
        'Type' : [],
        'Contact' : [],
        'adresse' : []
        

    }
def get_text(element):
    col = []
    for i in element:
        col.append(i.text)
    return col

# A function that ties it all together
def page_df(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    dom = etree.HTML(str(soup))
    titles = get_text(dom.xpath('//div[@class="establishment--search_item__content"]/h2'))
    print(titles)
    niveau_études = get_text(soup.find_all("span", {"class": "establishment-high-school establishment-type"}))
    try :
        type_ecole = get_text(soup.find_all("span", {"class": "establishment-public"}))
    except :
        type_ecole.append('NaN')
    print(type_ecole)
    adresse_ecole = get_text(dom.xpath('//div[@class="establishment--search_item__address"]/p[2]'))
    # mail_ecole = get_text(dom.xpath('//div[@class="establishment--search_item__address"]/p[last()]/a'))
    contact_ecole = get_text(soup.select('.establishment--search_item__address > p:last-child'))

    data['Nom Ecole'].extend(titles)
    data['Niveau'].extend(niveau_études)
    data['Type'].extend(type_ecole)
    data['adresse'].extend(adresse_ecole)
    data['Contact'].extend(contact_ecole)
    print(len(titles))
    print(len(niveau_études))
    print(len(type_ecole))
    print(len(adresse_ecole))
    print(len(contact_ecole))
    
"""for p in range(0,2) :
    print(f'page {p}')
    url = f'https://www.education.gouv.fr/annuaire?keywords=&department=&academy=1&status=All&establishment=All&geo_point=&page={p}'
    page_df(url)"""

url = f'https://www.education.gouv.fr/annuaire?keywords=&department=&academy=1&status=All&establishment=All&geo_point=&page={1}'
page_df(url)
"""df = pd.DataFrame(data)
df.to_csv('Ecoles.csv')"""