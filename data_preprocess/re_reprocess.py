#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月11日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
from pandas import DataFrame
from pandas import concat
import pandas as pd
time_ser_process=pd.read_csv('pricedetails_plus.csv')#准备进行时间序列处理
time_ser_process=time_ser_process.dropna(axis=0)
print(time_ser_process['citys'])
time_ser_process.to_csv('pricedetails_plus_1.csv')

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):#时间序列函数
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).
        dropnan: Boolean whether or not to drop rows with NaN values.
    Returns:
        Pandas DataFrame of series framed for supervised learning.
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg   
          
#print(time_ser_process.describe())
algname=time_ser_process['aglName'].drop_duplicates()
varietiesName=time_ser_process['varietiesName'].drop_duplicates()
time_ser_process['priceDate']=pd.to_datetime(time_ser_process['priceDate'])
#print(algname)
df = pd.DataFrame(columns = ["aglName", "bulkPrice ", "citys", "envir",'priceDate','product_class','season ','varietiesName','weather_condition','bulkPrice_day7','bulkPrice_day6','bulkPrice_day5','bulkPrice_day4','bulkPrice_day3','bulkPrice_day2','bulkPrice_day1',])
for i in list(algname):
    #print(i)
    data= time_ser_process[time_ser_process['aglName']==i]
    #print(data)
    data_1=data['varietiesName'].drop_duplicates()
    #print(data_1)
    
    for j in varietiesName:
        print(j)
        if(j in list(data_1)):
             data1=data[data['varietiesName']==str(j)]
             #print(data1['priceDate'])
             #data1['priceDate']=pd.to_datetime(data1['priceDate'])
             #data1=data1.sort_index(inplace=True)
             data1=data1.sort_values('priceDate')
             bulkprice=list(data1['bulkPrice'])
             #print(bulkprice)
             bulkprice=series_to_supervised(bulkprice, n_in=7, n_out=1, dropnan=False)
             bulkprice=pd.DataFrame(bulkprice)
             #print(bulkprice)
             bulkprice.columns=['bulkPrice_day7','bulkPrice_day6','bulkPrice_day5','bulkPrice_day4','bulkPrice_day3','bulkPrice_day2','bulkPrice_day1','bulkPrice']
             #print(bulkprice)
             #print(bulkprice)
             #bulkprice=pd.DataFrame(bulkprice,columns=['bulkPrice_day7','bulkPrice_day6','bulkPrice_day5','bulkPrice_day4','bulkPrice_day3','bulkPrice_day2','bulkPrice_day1','bulkPrice'])
             #print(bulkprice)
             bulkprice=bulkprice[['bulkPrice_day7','bulkPrice_day6','bulkPrice_day5','bulkPrice_day4','bulkPrice_day3','bulkPrice_day2','bulkPrice_day1']]
             #data1=data1.append(bulkprice)
             data1=pd.concat([data1,bulkprice],axis=1)
            
             df=df.append(data1)
             print(df)
        else :
            continue
df.to_csv(r'data1.csv')    





 

        
        
