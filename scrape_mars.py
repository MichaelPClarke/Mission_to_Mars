#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:49:32 2020

@author: Michael Clarke
"""
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


#def init_browser():
    #ON A MAC
 #   executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
  #  return Browser("chrome", **executable_path, headless=False)

def scrape():
    #ON A MAC
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'http://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    
    results = soup.find('ul', class_="item_list")
    #print(f'LOOK HERE {results}')
    #titles = []
    #teasers = []
    
 
    news_title = results.find('div', class_='content_title').text
    #titles.append(title)
        
    
    news_p = results.find('div', class_='article_teaser_body').text
    #date = results.find('div', class_='list_date').text
    
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(3)    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image_url = soup.find('a', class_="fancybox")['data-fancybox-href']
    featured_image_url = f"https://www.jpl.nasa.gov{image_url}"
 
    import GetOldTweets3 as got
    
    username = 'MarsWxReport'
    count = 1
    
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                            .setMaxTweets(count)
    
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
   
    for tweet in tweets:
        
        mars_weather=tweet.text
    
    url3 = 'https://space-facts.com/mars/'
    browser.visit(url3)
    time.sleep(3)    
    html=browser.html
    soup = BeautifulSoup(html,'html.parser')
    
    facts = pd.read_html(url3)
    facts = facts[0]
    facts.columns = ['Mars Key', ' Mars Value']
    facts
    
    facts.to_html()
    
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls = []
    browser.visit(url4)
    time.sleep(3)    
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    
    hemispheres_div = soup.find_all('div', class_='item')
    
    for hemi in hemispheres_div:
        hemi_name = hemi.find('h3').text
        
        imgurl = hemi.find('a', class_='itemLink product-item')
        browser.visit('https://astrogeology.usgs.gov' + imgurl['href'])
        time.sleep(3)     
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        hemi_image = soup.find('img', class_='wide-image')
        
        img_url2 = ('https://astrogeology.usgs.gov' + hemi_image['src'])
        hemisphere_image_urls.append({'title': hemi_name, 'img_url': img_url2})
       

    
    mars_data = {
        "Mars News Titles": news_title,
        "Mars News Details": news_p,
        "Latest Mars Image": featured_image_url,
        "Latest Mars Weather": mars_weather,
        "Hemisphere Images": hemisphere_image_urls
        }
    print(mars_data)
    

        
        
    
    return mars_data
#scrape()
