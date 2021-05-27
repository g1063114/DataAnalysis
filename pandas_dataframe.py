import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('./train.csv')

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

#train_data = pd.read_csv('./train.csv', usecols=['Survived','Name'])
#print(train_data)

#print(train_data[['Name','Age','Survived']])   # column 기준으로 잘라서 가져오는것

#print(train_data[7:10])        # row로 잘라서 가져오는것 slicing

#train_data.index = np.arange(100,991)
#print(train_data.head())

#print(train_data.loc[[101,102]])    # 지정한 index
#print(train_data.iloc[[0,1]])       # 0 base index

#print(train_data.loc[[100,200],['Survived','Name']])    # loc이기 때문에 지정한 row, column 가져올수 있음
#print(train_data.iloc[[0,2],[1,3]])                     # iloc이기 때문에 0 base index로 row, column 가져올수 있음

#class_ = train_data['Pclass'] == 1
#age_ = (train_data['Age'] >= 30) & (train_data['Age'] < 40)

#print(train_data[class_ & age_])       # boolean indexing 가능... 쿼리에서 where 절 사용하는것과 비슷

# train_data['Age_double'] = train_data['Age'] * 2
# print(train_data)
#train_data.insert(3,'Fare10',train_data['Fare'] / 10)       # 특정 위치에 컬럼 추가 가능
#print(train_data.head())

#print(train_data.drop('Fare10',axis=1))                 # 복사본에서 지워지는 것... 원본에는 영향 없음
#print(train_data.head())

#print(train_data.drop('Fare10',axis=1,inplace=True))    # 원본에도 영향 주는 속성
#print(train_data.head())

#print(train_data.corr())                    # 컬림 사이의 상관계수  -1 ~ 1 값을 가지는데 1로 갈수록 서로 비슷하게 증가, -1에 가까울수록 하나가 증가하고 하나는 감소한다.
#plt.matshow(train_data.corr())  
#plt.show()

#print(train_data.info())         # info 함수를 통해 간단히 값의 nan 확인이 가능하다.
#print(train_data.isna())         # isna 함수를 통해 boolean dataframe 생성하고 값이 true 이면 nan
#print(train_data['Age'].isna())

#print(train_data.dropna())         # row 기반으로 어떤 데이터가 하나라도 nan이 있으면 해당 row 지움 (복사본)
#print(train_data.dropna(subset=['Age']))   # Age 컬럼에 대해서만 nan 확인 후 지움
#print(train_data.dropna(axis=1))        # 컬럼 중에 nan 값이 있는 컬럼은 지움

#print(train_data['Age'].fillna(train_data['Age'].mean()))      # age 컬럼 데이터의 평균으로 nan값 대체
surv_mean = train_data[train_data['Survived'] == 1]['Age'].mean()       # 생존자 필터링 한 평균값
death_mean = train_data[train_data['Survived'] != 1]['Age'].mean()      # 사망자 필터링 한 평균값
print(train_data[train_data['Survived'] == 1]['Age'].fillna(surv_mean))
print(train_data[train_data['Survived'] != 1]['Age'].fillna(death_mean))
