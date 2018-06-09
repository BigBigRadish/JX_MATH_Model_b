#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月8日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
from bs4 import BeautifulSoup
from datetime import datetime
import threading
import requests
import urllib.request;
import time
import random
import json
import re
import redis
import pymysql 
from pymongo import MongoClient
import DBUtils
from DBUtils.PooledDB import PooledDB
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQ'
headers={'User-Agent':user_agent}
url="http://www.chinaapm-data.com/mn/md"
#pool = PooledDB(pymysql,5,host='localhost',user='root',passwd='147258',db='math_model',port=3306,charset='utf8mb4') #5为连接池里的最少连接数
con=MongoClient('localhost', 27017)
db=con.modelData
collection=db.marketData
data = open("marketDy.json")
data=json.load(data)
print(data)
import re
def collect_data(data):
    for i in range(len(data)):
        publishUser=data[i]["publishUser"]
        publishAt=data[i]["publishAt"]
        #articleTypeId=data[i]["articleTypeId"]
        id=data[i]["id"]
        title=data[i]["title"]
        url=r'http://www.chinaapm-data.com/mn/mdc/'+str(id)
        article=article_collect(url)
        marketDetails={"publishUser":publishUser,"publishAtTime":publishAt,"id":id,"title":title,"article":article}
        collection.insert(marketDetails)
        
def article_collect(url):
    r = requests.get(url,headers=headers)  
    soup = BeautifulSoup(r.text,'html.parser')#html.parser
    print(soup)
    data=soup.find(class_='content3').find_all('p')
    pattern = re.compile(r'<p>(.*)</p>') 
    data=pattern.findall(str(data))
    print(data)
    data=''.join(data)
    return data
if __name__ == '__main__':   
    collect_data(data) 
      