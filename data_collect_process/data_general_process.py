#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月9日

@author: Zhukun Luo
Jiangxi university of finance and economics
数据合并
'''
import pandas as pd
import re
from docopt import Pattern
#from data_collect_process.history_weather_collect import parttern
#pricedata=pd.read_csv(r'C:\Users\Agnostic\Desktop\pricedetails.csv')
#varietiesName=pd.DataFrame(pricedata)['varietiesName'].drop_duplicates() 
#varietiesName.to_csv('varietiesName.csv')
def process_condition():
    weather_condition=weatherdata['weather_condition']
    list=[]
    print(weather_condition[1])#处理天气
    for i in weather_condition:
        print(i)
        i=i.replace(' ','').replace('\n','').replace('\r','')
        parttern=re.compile(r'^(.*)\/') 
        print(parttern.findall(i))
        i=parttern.findall(i).strip()
        print (i)
        i=''.join(i)
        list.append(i)
    weatherdata['weather_condition']=list  
    print(weatherdata['weather_condition'])
    weatherdata.to_csv('weather.csv')
def date_process():   #日期处理
    date=weatherdata['priceDate']      
    print(date) 
    parttern1=re.compile(r'^(.*)年')
    parttern2=re.compile(r'年(.*)月')
    parttern3=re.compile(r'月(.*)日')
    for date in date:
        year=''.join(parttern1.findall(date))
        month=''.join(parttern2.findall(date))
        if ('0' in month):
            month=month.replace('0','')
        day=''.join(parttern3.findall(date))
        if ('0' == day[0]):
            day[0]=''
        #print(year+'/'+month+'/'+day)
        list.append(year+'/'+month+'/'+day)
def condition_reprocess():
    list=[]
    conditions=weatherdata['weather_condition']
    for i in conditions:
        i= i.replace("['",'').replace("']",'')
        print (i)
        list.append(i)
    weatherdata['weather_condition']=list
    weatherdata.to_csv('weather.csv')
def weather_price_process():
   weather_price1=weather_price.dropna()
   weather_price1.to_csv('weather_price.csv')
def  weather_10_process():
    list=[]
    for i in weather_10_process1['priceDate']:
       a= i.replace('2017/1','2017/10') 
       list.append(a)
    weather_10_process1['priceDate']=list
    weather_10_process1.to_csv('weatehr_patch.csv')
if __name__ == '__main__': 
    list=[]
    weatherdata=pd.read_csv(r'C:\Users\Agnostic\Desktop\weather.csv',encoding='utf8')
    weather_price=pd.read_csv(r'C:\Users\Agnostic\Desktop\preprocess\weather_price.csv',encoding='utf8')
    weather_10_process1=pd.read_csv(r'weather_patch.csv')
    #date_process()  
    #process_condition() 
    #condition_reprocess()
    weather_price_process()
    #weather_10_process()
   # weather=pd.read_csv('weather.csv')
    #print(weather)
    
   
    


        
