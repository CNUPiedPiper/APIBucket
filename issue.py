#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def get_issue():
    url = urllib2.urlopen('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
    soup = BeautifulSoup(url, 'html.parser')
    result = soup.find_all('ul')

    issue_data = list()

    for res in result:
        if res['class'][0] == 'rank_list':
            keywords = res.find_all('span')
            for key in keywords:
                issue_data.append(key.contents[0])
            break

    return issue_data

