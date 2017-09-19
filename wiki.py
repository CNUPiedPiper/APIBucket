import wikipedia as wk
import sys

def get_wiki(title):
    wk.set_lang('ko')
    try: 
        summary = wk.summary(title, sentences=2)
    except wikipedia.exceptions.DisambiguationError as ed:
        return ed.options
    except wikipedia.exceptions.PageError as ep: 
        retrun u'해당 정보가 없습니다.'
    return summary

if __name__== '__main__" : 
    print get_wiki(sys.argv[1])

