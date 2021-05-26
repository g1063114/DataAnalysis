import numpy as np
import pandas as pd

#train_data = pd.read_csv('./train.csv')

#print(train_data.head())
#print(train_data.shape)    
#print(train_data.describe())   # 한눈에 간단하게 통계치 확인할 수 있는 함수
#print(train_data.info())


# data = {'a':100,'b':200,'c':300}
# print(pd.DataFrame(data, index=['x','y','z']))


# data2 = {'a':[1,2,3],'b':[4,5,6],'c':[10,11,12]}
# print(pd.DataFrame(data2, index=['x','y','z']))

# a = pd.Series([100,200,300],['a','b','c'])
# b = pd.Series([101,201,301],['a','b','c'])
# c = pd.Series([105,205,305],['a','b','c'])

# print(pd.DataFrame([a,b,c]))

# train_data = pd.read_csv('./train.csv', sep=',')
# print(train_data)

# train_data = pd.read_csv('./train.csv', index_col='PassengerId')
# print(train_data)

train_data = pd.read_csv('./train.csv', usecols=['Survived','Name'])
print(train_data)