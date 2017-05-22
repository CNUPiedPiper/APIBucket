#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
soup = BeautifulSoup(url, 'html.parser')

result = soup.find_all('ul')

for res in result:
    if res['class'][0] == 'rank_list':
        keywords = res.find_all('span')
        for key in keywords:
            print key.contents[0]
        break

