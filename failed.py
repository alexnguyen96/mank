# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:54:45 2020

@author: Alex Nguyen
"""
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup
'''
from selenium import webdriver

site = 'https://www.thewhitewinecameupwiththefish.com/1'
directory = "C:/Users/Alex Nguyen/Downloads/wine/" #Relative to script location

driver = webdriver.Chrome('C:/Users/Alex Nguyen/Downloads/chromedriver_win32')


driver.get(site)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_tags = soup.findAll("div", {"class": "_image_224db _ready_224db"})

urls = [img['style'] for img in img_tags]

for url in urls:
    print(url)
    '''
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)

    with open(os.path.join(directory, filename.group(1)), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
        '''
'''
https://nflx-microsite-pub-twwcuwtf-uploads-prod.s3.us-west-2.amazonaws.com/variants/TCLySnGgWmZNQFPVCxk6RjQX/397b2d2fecfae60cf0bd612c9c3e33039493936b7d05fb24f28058aee9918102
https://nflx-microsite-pub-twwcuwtf-uploads-prod.s3.us-west-2.amazonaws.com/variants/W7p2USHrebY1CNBLVsZaFPVk/397b2d2fecfae60cf0bd612c9c3e33039493936b7d05fb24f28058aee9918102
'''