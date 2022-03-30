import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pandas as pd

data = {
    'Name' : [],
    'Platform' : [],
    'Year' : [],
    'Review' : []
}

#browser = webdriver.Chrome('chemin_vers_votre_chrome_driver')
browser = webdriver.Chrome('C:\\Users\\Yassine\\Documents\\Python_Projects\\Beginner\\basics\\chromedriver.exe')
browser.get('https://www.education.gouv.fr/annuaire?keywords=&department=&academy=1&status=All&establishment=All&geo_point=&page=0')
time.sleep(3)
# nom ecole 

button = browser.find_element_by_xpath('//*[@id="block-edugouv-theme-content"]/div/div[1]/div[2]/div[2]/div[2]/div/a')
button.click()


"""nom_ecole_html = browser.find_elements_by_xpath('//*[@class="establishment--search_item__content"]/h2')
list_nom_ecole = [x.text for x in nom_ecole_html]
cordonnées_ecole_html = browser.find_elements_by_xpath('//div[@class="establishment--search_item__address"]/p[2]')
list_cordonnées_ecole = [x.text for x in cordonnées_ecole_html]
email_ecole_html = browser.find_elements_by_xpath('//div[@class="establishment--search_item__address"]/p[last()]/a')
list_email_ecole = [x.text for x in email_ecole_html]
tel_ecole_html = browser.find_elements_by_xpath('//div[@class="establishment--search_item__address"]/p[last()]/following-sibling::text()')
list_tel_ecole = [x.text for x in tel_ecole_html]
# //*[@id="block-edugouv-theme-content"]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[1]/p[4]/text()
print(list_tel_ecole)"""
browser.close()