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
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
#pool = PooledDB(pymysql,5,host='localhost',user='root',passwd='147258',db='math_model',port=3306,charset='utf8mb4') #5为连接池里的最少连接数
#conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了 
import re    
def price_collect(url):
    html = urllib.request.urlopen(url).read().decode('utf8') 
    html=html[43:-32]
    data=json.loads(html)#json的数据格式
    for i in range(len(data)):
        priceDate=data[i]['priceDate']#产品日期
        varietiesName=data[i]['varietiesName']#产品名
        bulkPrice=data[i]['bulkPrice']#产品价格
        aglName=data[i]['aglName']#售卖市场
        connectMysql(conn, priceDate, varietiesName, bulkPrice, aglName)

def connectMysql(connection,priceDate,varietiesName,bulkPrice,aglName):#连接数据库并插入数据
#获取会话指针
    with connection.cursor() as cursor:
#创建sql语句
        sql = "insert into `priceDetails` (`priceDate`,`varietiesName`,`bulkPrice`,`aglName`) values (%s,%s,%s,%s)"
#执行sql语句
        cursor.execute(sql,(priceDate,varietiesName,bulkPrice,aglName))
#提交数据库
        connection.commit()
        
if __name__ == '__main__': 
    conn = pymysql.connect(host='127.0.0.1', user='root', password='147258', db='math_model', charset='utf8mb4')
    url="http://www.chinaapm-data.com/pq/findByPage?draw=2&columns%5B0%5D%5Bdata%5D=varietiesName&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=priceDate&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=bulkPrice&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=aglName&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=trendUri&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=233811&search%5Bvalue%5D=&search%5Bregex%5D=false&startTime=2017-06-08&endTime=2018-06-08&marketCode=&varietiesCode=&province=&typeCode=&_=1528469159849"#构造url链接  
    price_collect(url)
    conn.close()