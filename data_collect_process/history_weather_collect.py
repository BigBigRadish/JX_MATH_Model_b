#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月9日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
from bs4 import BeautifulSoup
import re
import requests
from pymongo import MongoClient
citylist=['anqing','baotou','changsha','changzhou','chaoyang','dalian','fuzhou','ganzhou','guangzhou','hefei','hengyang','huhehaote','huangshan','jingzhou','mianyang','nanchang','nanjing','nanning','qingdao','shangqiu','shanghai','shenzhen','shijiazhuang','shouguang','suzhou','taiyuan','taizhou','tianjin','tianshui','wulumuqi','wuhan','xian','xuancheng','yinchuan','yuxi','chongqing']
monthlist=['201707','201708','201709','201710','201711','201712','201801','201802','201803','201804','201805']
con=MongoClient('localhost', 27017)
db=con.modelData
collection=db.weatherData
for j in monthlist:
    for i in range(len(citylist)):
        city=citylist[i-1]
        url='http://www.tianqihoubao.com/lishi/'+citylist[i-1]+'/month/'+str(j)+'.html'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQ'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers) 
        soup = BeautifulSoup(r.text,'html5lib')#html.parser
        #print (soup)
        tr=soup.find_all('tr')[8]
        td=tr.find_all('td')
        print(td)
        priceDate=td[0].text.strip()#日期
        weather_condition=td[1].text.strip()#天气状况
        parttern=re.compile('(.*)℃')
        envir =parttern.findall(td[2].text.strip())[1]#
        print(envir)
        weatherDetails={"priceDate":priceDate,"weather_condition":weather_condition,"envir":envir,'city':city}
        #collection.insert(weatherDetails)
#         for idx, tr in enumerate(soup.find_all('tr')):
#             if idx != 0:
#                 td=tr.find_all('td')
#                 print(td)
#                 priceDate=td[0].text.strip()#日期
#                 weather_condition=td[1].text.strip()#天气状况
#                 parttern=re.compile('(.*)℃')
#                 try:
#                     envir =parttern.findall(td[2].text.strip())[1]#
#                     print(envir)
#                 except IndexError as e:
#                     continue
#                 
#                 weatherDetails={"priceDate":priceDate,"weather_condition":weather_condition,"envir":envir,'city':city}
#                 collection.insert(weatherDetails)