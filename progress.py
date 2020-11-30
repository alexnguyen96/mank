# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:33:49 2020

@author: Alex Nguyen
"""
import requests
from bs4 import BeautifulSoup as bs
import re


def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    meta = soup.find("meta", property="og:image")
    #print(meta['content'])
    content = re.search('^.*/variants/[A-Za-z][A-Za-z0-9]*/', meta['content'])
    if content is not None: #if not none, then the image exists
        key = content.group(0)
        #print(key)
        url = key + "397b2d2fecfae60cf0bd612c9c3e33039493936b7d05fb24f28058aee9918102"
        #print(url)
        
        ######## TODO: use the key to save the image
        
    else: #else, its a video,
        #let save the html and see the link
        with open("video.html", "w", encoding='utf-8') as file:
            file.write(str(soup))
        
        ## TODO: add code to download the videos which are from vimeo
        ## right now, i'll just manually download them because there are not that many
        
    
get_all_images("https://www.thewhitewinecameupwiththefish.com/21")

######## TODO: make the loop to go through all the webpage
