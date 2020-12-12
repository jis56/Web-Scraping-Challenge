import requests
import pymongo
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    executable_path = {'executable_path': r"C:\Chromedrive\chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape_info(browser):

    #News
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    #Image

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    time.sleep(1)

    browser.click_link_by_id('full_image')
    browser.click_link_by_partial_text('more info') 

    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')

    image = image_soup.body.find("figure", class_="lede")
    href = image.find('a')['href']

    base_url='https://www.jpl.nasa.gov'

    featured_image_url = base_url + href

    #Facts Table

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    time.sleep(1)

    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns = [" ", "Mars"]

    facts_html=facts_df.to_html(index=False)

    #Hemispheres

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    time.sleep(1)

    #Cerebus

    browser.click_link_by_partial_text('Cerberus')
    browser.click_link_by_partial_text('Open')

    hemisphere_html = browser.html
    cerberus_soup = BeautifulSoup(hemisphere_html, 'html.parser')

    cerberus_img = cerberus_soup.body.find('img', class_ = 'wide-image')['src']

    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    cerberus_url = hemisphere_base_url + cerberus_img

    browser.visit(mars_hemispheres_url)
    time.sleep(1)

    #Schiaparelli

    browser.click_link_by_partial_text('Schiaparelli')
    browser.click_link_by_partial_text('Open')

    hemisphere_schia_html = browser.html
    schia_soup = BeautifulSoup(hemisphere_schia_html, 'html.parser')

    schia_img = schia_soup.body.find('img', class_ = 'wide-image')['src']
    schia_url = hemisphere_base_url + schia_img

    browser.visit(mars_hemispheres_url)

    time.sleep(1)

    #Syrtis Major

    browser.click_link_by_partial_text('Syrtis Major')
    browser.click_link_by_partial_text('Open')

    hemisphere_sm_html = browser.html
    sm_soup = BeautifulSoup(hemisphere_sm_html, 'html.parser')

    sm_img = sm_soup.body.find('img', class_ = 'wide-image')['src']

    sm_url = hemisphere_base_url + sm_img

    browser.visit(mars_hemispheres_url)

    time.sleep(1)

    #Valles Marineris

    browser.click_link_by_partial_text('Valles Marineris')
    browser.click_link_by_partial_text('Open')

    hemisphere_vm_html = browser.html
    vm_soup = BeautifulSoup(hemisphere_vm_html, 'html.parser')

    vm_img = vm_soup.body.find('img', class_ = 'wide-image')['src']

    vm_url = hemisphere_base_url + vm_img

    hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": vm_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schia_url},
        {"title": "Syrtis Major Hemisphere", "img_url": sm_url}
    ]

    return {"news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "facts_html": facts_html,
            "hemispheres_image_urls":hemispheres_image_urls
            }
    browser.quit()


print(scrape_info(init_browser()))