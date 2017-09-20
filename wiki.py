#-*- coding: utf-8 -*- 
import wikipedia as wk
import sys

def get_wiki(title):
    wk.set_lang('ko')
    try: 
        summary = wk.summary(title, sentences=2)
    except wk.exceptions.DisambiguationError as ed:
        return wk.summary(ed.options[0], sentences=2)
    except wk.exceptions.PageError as ep: 
        return u'해당 정보가 없습니다.'
        
    return summary

if __name__== '__main__' : 
    print get_wiki(sys.argv[1])

