#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月10日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd
import jieba
import jieba,math
import jieba.analyse
import jieba.posseg as psg
import re
from pymongo import MongoClient
con=MongoClient('localhost', 27017)
db = con.modelData
collection=db.wordDetail
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'rb').readlines()]  
    return stopwords 
def seg_sentence(sentence):  
    sentence_seged = psg.cut(sentence.strip())  
    stopwords = stopwordslist('哈工大停用词表.txt')  # 这里加载停用词的路径  
    outstr = ''
    word_freq = {}  
    for ele in sentence_seged:  
        if ele.word not in stopwords:  
            if ele in word_freq:
                word_freq[ele] += 1
            else:
                word_freq[ele] = 1
    freq_word = []
    for ele, freq in word_freq.items():
        freq_word.append((ele.word, ele.flag,freq))
    freq_word.sort(key = lambda x: x[1], reverse = True)
    for ele.word, ele.flag,freq in freq_word:
        word=ele.word;
        flag=ele.flag
        freq=freq;
        wordDetail = {"word":word,"flag":flag,"freq":freq}
        collection.insert(wordDetail)
if __name__ == '__main__':
    article=pd.read_csv(r'C:\Users\Agnostic\Desktop\marketData.csv',encoding='utf8')
    words=''
    print(article['title'])
    for title in article['title']:
        if(':' in str(title)):
            title=title.replace(':','')
        words+=str(title)
    print(words)
    seg_sentence(words)
    
    