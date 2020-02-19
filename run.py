# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:09:47 2020

@author: frohlict
"""

from requests import get
from bs4 import BeautifulSoup    
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly as py
import plotly.graph_objs as go
import chart_studio.plotly as ply






import plotly.express as px


import time
# pip install lxml


url1 = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&ref_=adv_prv"
url2 = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&start=51&ref_=adv_nxt"
url3 = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&start=101&ref_=adv_nxt"
url4 = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&start=151&ref_=adv_nxt"
links = [url1, url2, url3, url4]  #  , url2, url3, url4



# website urls
#url = "https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&start=151&ref_=adv_nxt"
#"https://www.imdb.com/search/title/?locations=Regina,%20Saskatchewan&view=advanced"




names = []
ratings = []
votess = []
episodes = []



for link in links: 


    response = get(link)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    stuff = html_soup.find_all('div', class_ = 'lister-item mode-advanced')




    for item in stuff:
        name = item.h3.a.text
        #names.append(name)


        xyz = item.h3.find_all('a')    # this gives us a list.  the 2nd item contains the episode.....[<a href="/title/tt0397138/"> Corner Gas</a>, <a href="/title/tt0546118/">I Love Lacey</a>]



        rating_check = item.find('strong')
        if rating_check is None:
            rating = "N/A"
            #ratings.append(rating)
        else:
            rating = item.strong.text
            #ratings.append(rating)

        vote_check = item.find('span', attrs = {'name':'nv'})
        if vote_check is None:
           votes = 0
            #votess.append(votes)
        else:
            votes = int(item.find('span', attrs = {'name':'nv'})['data-value'])
            #votess.append(votes)
            
        # this ensures we dont get any episodes in list    
        if len(xyz) < 2:
            z = "No Episode"
            episodes.append(z)
            names.append(name)
            ratings.append(rating)
            votess.append(votes)


        #else:
        #    z =xyz[1].text
        #    episodes.append(z)
        #    names.append(name)
        #    ratings.append(rating)
        #    votess.append(votes)
            
        print ('MOVIE: ', name, 'RATING: ', rating, 'VOTES: ', votes, 'EPISODE: ', z)     #epis
        
    time.sleep(4)
    
movie_ratings = pd.DataFrame({'MOVIE': names, 'RATING': ratings, 'VOTES': votess, 'EPISODE': episodes})
movie_ratings.style.set_properties(**{'text-align': 'left'})

movie_ratings.query('VOTES > 0', inplace = True)



fig = px.bar(movie_ratings, x='MOVIE', y='RATING',
             hover_data=['MOVIE', 'RATING', 'VOTES'],
             category_orders={'VOTES'})

fig.update_layout(height=1000, width=1000, title_text='Movies shot in Regina Ratings')

py.offline.plot(fig, filename='basic-bar1.html')


print (movie_ratings)

















