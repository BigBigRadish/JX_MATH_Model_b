#!/home/admin/anaconda3/envs/TF/bin/ python3.5
# -*- coding: utf-8 -*- 
'''
Created on 2018年6月11日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.metrics as sm
from sklearn.preprocessing import  OneHotEncoder#onehot对独立型特征进行编码
from sklearn.linear_model import LassoCV
from sklearn.cross_validation import train_test_split 
from tpot import TPOTRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR 
from sklearn.tree import  DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from mlxtend.regressor import StackingRegressor
import matplotlib.pyplot as pl 
from sklearn.linear_model import MultiTaskLasso, Lasso
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LassoCV

dataset=pd.read_csv(r'weather_price_density.csv')
#print(dataset.isnull())
dataset=pd.get_dummies(dataset,columns=['city','month','product_class','province','season','varietiesName','weather_condition']) 
#print(dataset)
#dataset.to_csv(r'C:\Users\Agnostic\Desktop\dataset_onehot.csv',encoding='utf8')
dataset['priceDate']=pd.to_datetime(dataset['priceDate'])
#print(dataset.head(10))
#print(dataset[dataset['priceDate']=='2017-12'].head(10))
use_set=pd.read_csv(r'dataset_onehot_use_set.csv')
validate_set=pd.read_csv(r'dataset_onehot_validate_set.csv')
predict_y=validate_set['bulkPrice']
predict_x=validate_set.drop(columns=['bulkPrice'])
#print(use_set.describe())
target=use_set['bulkPrice']
print(target)
train_data=use_set.drop(columns=['bulkPrice'])
#print(train_data.head(10))
train_X, test_X, train_y, test_y  = train_test_split(train_data,  #划分训练集
                                                   target,  
                                                   test_size = 0.1,  
                                                   random_state = 0)
#params = [1]
#test_scores = []
#for param in params:
    #clf = XGBRegressor( learning_rate=0.1, max_depth=param, min_child_weight=2)#效果一搬 #56%max_depth=1
#     clf=GradientBoostingRegressor(loss='ls', alpha=0.9,#40%
#                                             n_estimators=500,
#                                             learning_rate=0.05,
#                                             max_depth=1,
#                                             subsample=0.8,
#                                             min_samples_split=9,
#                                             max_leaf_nodes=10)#这方法也不行
#model_lasso = LassoCV(alphas = [1, 0.1, 0.001, 0.0005]).fit(train_X, train_y) # 此处 alpha 为通常值 #fit 把数据套进模型里跑
# lr = LinearRegression()#效果不好不到50%
# rfg = RandomForestRegressor(bootstrap=True, max_features=0.005, min_samples_leaf=11, min_samples_split=10,
#                                         n_estimators=100)#最高59%
# 
# svr_rbf = SVR(kernel='rbf')
# clf=svr_rbf#跑不出来。。。我擦
# stregr = StackingRegressor(regressors=[las, las, las, las], meta_regressor=svr_rbf)
# test_score = np.sqrt(-cross_val_score(las, test_X, test_y, cv=10, scoring='neg_mean_squared_error'))#70%的正确率,与lasso差不多
# print(test_score)    
#pl.plot(params, test_scores)
#pl.title("max_depth vs CV Error");
#pl.show()
#此路不通
###########2.回归部分##########
def try_different_method(model):
    model.fit(train_X,train_y)
     # 打印最优的α值
    #print ("最优的alpha值: "+str(lassocv.alpha_.astype('float')))
    # 打印模型的系数
    #print (lassocv.intercept_)
    #print (lassocv.coef_)
     #score = model.score(test_X, test_y)
    result = model.predict(predict_x)
    print('mean absolute error=',round(sm.mean_absolute_error(predict_y,result),2))
    print('mean squared error=',round(sm.mean_squared_error(predict_y,result),2))
    print('median absolute error=',round(sm.median_absolute_error(predict_y,result),2))
    print('explained variance score=',round(sm.explained_variance_score(predict_y,result),2))
    model_compair_data=pd.DataFrame(columns=['predict_y','true_y'])
    model_compair_data['predict_y']=result
    model_compair_data['true_y']=predict_y
    model_compair_data.to_csv('XGB_compair.csv')#存储真实值与预测值比对结果集
    #print('R2 score=',round(sm.r2_score(test_y,result),2)
#     plt.figure()
#     plt.plot(np.arange(len(result)), test_y,'go-',label='true value')
#     plt.plot(np.arange(len(result)),result,'ro-',label='predict value')
#     plt.title('score: %f'%score)
#     plt.legend()
#     plt.show()
#     score1 = model.score(predict_x, predict_y)
#     result1 = model.predict(predict_x)
#     plt.figure()
#     plt.plot(np.arange(len(result1)), predict_y,'go-',label='true value')
#     plt.plot(np.arange(len(result1)),result1,'ro-',label='predict value')
#     plt.title('score: %f'%score1)
#     plt.legend()
#     plt.show()
    #print(cross_val_score(model, train_X, train_y, cv=10))
def get_index():
    pass
from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()
####3.2线性回归####
from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()
####3.3SVM回归####
from sklearn import svm
model_SVR = svm.SVR()
####3.4KNN回归####
from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()
####3.5随机森林回归####
from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)#这里使用20个决策树,也不错
####3.6Adaboost回归####
from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)#这里使用50个决策树，效果也不错
####3.7GBRT回归####
from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)#这里使用100个决策树
####3.8Bagging回归####
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
####3.9ExtraTree极端随机树回归####
from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()
from xgboost import XGBRegressor
model_XgbRegressor=XGBRegressor()
lassocv = LassoCV(alphas=[0.01, 0.1, 0.5, 1, 3, 5, 7, 10, 20, 100], cv=5)

###########4.具体方法调用部分##########
try_different_method(model_XgbRegressor)
#regr_1 = tree.DecisionTreeRegressor(max_depth=2)#lsd作为衡量标准
#regr_2 = tree.DecisionTreeRegressor(max_depth=5)
#regr_3 = tree.DecisionTreeRegressor(max_depth=8)
#regr_1.fit(train_X, train_y)
#regr_2.fit(train_X, train_y)
#regr_3.fit(train_X, train_y)

# Predict
#X_test = np.arange(0.0, 10.0, 0.01)[:, np.newaxis]
#y_1 = regr_1.predict(test_X)
#y_2 = regr_2.predict(test_X)
#y_3 = regr_3.predict(test_X)

# Plot the results
#plt.figure()
#plt.scatter(train_X, train_y, s=20, edgecolor="black",
            #c="darkorange", label="data")
#plt.plot(test_X, y_1, color="cornflowerblue",
         #label="max_depth=2", linewidth=2)
# plt.plot(test_X, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
# plt.plot(test_X, y_3, color="r", label="max_depth=8", linewidth=2)
#plt.xlabel("data")
#plt.ylabel("target")
#plt.title("Decision Tree Regression")
#plt.legend()