# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:40:23 2020

@author: frohlict
"""



from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get



# website urls
url = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&view=simple"
response = get(url)
print(response.text[:500])


html_soup = BeautifulSoup(response.text, 'html.parser')


title = html_soup.title
print(title)
print(html_soup.prettify())


text = html_soup.get_text()
print(html_soup.text)


#title working


for item1 in html_soup.find_all('div', class_ = 'col-title'):
        for item2 in item1.find_all('a'):
           if '/title' in item2['href']:
                print(item2.contents[0])


#imdb rating
imdb_rating = html_soup.find_all(class_ = 'col-imdb-rating')

for t1 in html_soup.find_all('div', class_ = 'col-imdb-rating'):
    for t2 in t1.find('strong'):
        print(t2)

# imdd votes




#justin


 

from bs4 import BeautifulSoup
from requests import get
import pandas as pd 
import plotly.graph_objects as go


 


# website urls
url = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&view=advanced"
response = get(url)

 


html_soup = BeautifulSoup(response.text, 'html.parser')

 

stuff = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

 

print(type(stuff))
print(len(stuff))


names = []
ratings = []
votess = []

 

for item in stuff:
    name = item.h3.a.text
    names.append(name)
    
    rating_check = item.find('strong')
    if rating_check is None:
        rating = "N/A"
        ratings.append(rating)
    else:
        rating = item.strong.text
        ratings.append(rating)

 

    vote_check = item.find('span', attrs = {'name':'nv'})
    if vote_check is None:
        votes = "N/A"
        votess.append(votes)
    else:
        votes = item.find('span', attrs = {'name':'nv'})['data-value']
        votess.append(votes)
        
        
    print ('MOVIE:  ', name, '    ', rating, '    ', votes)

movie_ratings = pd.DataFrame({'MOVIE': names, 'RATING': ratings, 'VOTES': votess})

movie_ratings.style.set_properties(**{'text-align': 'left'})

import plotly.express as px
fig = px.bar(movie_ratings, x='MOVIE', y='RATING')
py.offline.plot(fig, filename='basic-bar1.html')

