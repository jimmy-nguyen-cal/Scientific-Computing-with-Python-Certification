# Why Scrape?

# Pull data
# get your own data back out of some system that has no 'export capability'
# Monitor a site for new information
# Spider the web to make a database for a search engine

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ') #   http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# 'a' tag defines a hyperlink and what follows after is the href attribute
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
