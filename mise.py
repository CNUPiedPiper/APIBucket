#-*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import json

reload(sys)
sys.setdefaultencoding('utf-8')

convert_cityname = {'Seoul':u'서울','Busan':u'부산','Daegu':u'대구','Incheon':u'인천','Gwangju':u'광주','Daejeon':u'대전','Ulsan':u'울산','Gyeonggi':u'경기','Gangwon':u'강원','Chungbuk':u'충북','Chungnam':u'충남','Jeonbuk':u'전북','Jeonnam':u'전남','Gyeongbuk':u'경북','Gyeongnam':u'경남','Jeju':u'제주','Sejong':u'세종'}

convert_dust_level = {u'1':u'좋음',u'2':u'보통',u'3':u'나쁨',u'4':u'매우나쁨'}

def get_mise(city):
    
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    sidoName = convert_cityname[city]
    pageNo = "1"
    numOfRows = "10"
    apiKey = "Rq7qiY10CshLuLdOB0E5iqqaTH1%2BQ5ScQecqgW2orlJ5j678Zv8j85HwR3Eo8XX8Dg6fc%2Fp8o3XvInGI4HsfdA%3D%3D"
    version = "1.3"
    returnType = "json"

    params = urllib.urlencode({
            'sidoName': sidoName,
            'pageNo': pageNo,
            'numOfRows': numOfRows,
            'ver': version,
            '_returnType': returnType
    })
   
    params = params+"&ServiceKey="+apiKey

    data = urllib2.urlopen(url, params).read()
    data = json.loads(data)

    return "오늘 미세먼지 농도는 " + data["list"][1]["pm10Value"] + "이고 상태는" + convert_dust_level[data["list"][1]["pm10Value"] + "입니다."
