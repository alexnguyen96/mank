# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:33:49 2020

@author: Alex Nguyen
"""
import requests
from bs4 import BeautifulSoup as bs
import re


def get_all_images(i):
    
    directory = "C:/Users/Alex Nguyen/Downloads/mank/" 
    #######remember to change to your directory
    url = "https://www.thewhitewinecameupwiththefish.com/" + i
    soup = bs(requests.get(url).content, "html.parser")
    meta = soup.find("meta", property="og:image")
    #print(meta['content'])
    content = re.search('^.*/variants/[A-Za-z0-9]*/', meta['content'])
    if content is not None: #if not none, then the image exists
        key = content.group(0)
        #print(key)
        img_url = key + "397b2d2fecfae60cf0bd612c9c3e33039493936b7d05fb24f28058aee9918102"
        #print(url)
        
        myfile = requests.get(img_url, allow_redirects=True)
        output_file = directory + i
        
        with open(output_file, 'wb') as f:
            f.write(myfile.content)
        
    else: #else, its a video,
        #let save the html and see the link
        """
        with open("video.html", "w", encoding='utf-8') as file:
            file.write(str(soup))
        """
        print("this is a video ", i)
        ## TODO: add code to download the videos which are from vimeo
        ## right now, i'll just manually download them because there are not that many
        
for i in range(1, 213): #total pages is 212 so the end should be 213
    get_all_images(str(i))


'''
I checked on Trid, looks like all images are JPEG so I used the following code to add the extension
or you can just add extension to the code above


import os
path = 'C:/Users/Alex Nguyen/Downloads/wine_jpg/'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
'''
