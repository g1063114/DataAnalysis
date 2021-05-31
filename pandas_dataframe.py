import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

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
#surv_mean = train_data[train_data['Survived'] == 1]['Age'].mean()       # 생존자 필터링 한 평균값
#death_mean = train_data[train_data['Survived'] != 1]['Age'].mean()      # 사망자 필터링 한 평균값
#print(train_data[train_data['Survived'] == 1]['Age'].fillna(surv_mean))
#print(train_data[train_data['Survived'] != 1]['Age'].fillna(death_mean))


#train_data['Pclass'] = train_data['Pclass'].astype(str)     
#print(train_data.info())

def age_categorize(age):
    if math.isnan(age):
        return -1
    return math.floor(age / 10) * 10

#print(train_data['Age'].apply(age_categorize))     # 해당 컬럼에 일괄적으로 적용해야 할 때 apply 함수에 파라미터로 함수 넣어준다.

# one-hot-encoding ( 범주형 데이터 -> 숫자형 데이터 ) 전체 범주가 column이 되고 해당하는 것은 1 아니면 0으로 변환
#print(pd.get_dummies(train_data, columns=['Pclass','Sex','Embarked']))      # 음 약간 피벗팅이랑 비슷한??

class_group = train_data.groupby('Pclass')

#print(class_group.groups)

gender_group = train_data.groupby('Sex')

#rint(gender_group.groups)

#print(class_group.count())
#print(class_group.mean()['Age'])

#print(gender_group.mean()['Survived'])

#print(train_data.groupby(['Pclass','Sex']).mean()['Survived'])

#print(train_data.set_index(['Pclass','Sex']).reset_index())

#print(train_data.set_index('Age').groupby(level=0).mean())

#print(train_data.set_index('Age').groupby(age_categorize).mean()['Survived'])

#print(train_data.set_index(['Pclass','Sex']).groupby(level=[0,1]).mean()['Age'])

#print(train_data.set_index(['Pclass','Sex']).groupby(level=[0,1]).aggregate([np.mean,np.sum,np.max]))

#print(train_data.groupby('Pclass').mean())      # Pclass에 대한 groupby로 인해 row가 3개가 된다 ( pclass 값이 1 2 3 이기때문에)
#print(train_data.groupby('Pclass').transform(np.mean))  # 원본 데이터에 groupby 한 값들로 채워지게 된다

df = pd.DataFrame({
    '지역':['서울','서울','서울','경기','경기','부산','서울','서울','부산','경기','경기','경기'],
    '요일':['월요일','화요일','수요일','월요일','화요일','월요일','목요일','금요일','화요일','수요일','목요일','금요일'],
    '강수량':[100,80,1000,200,200,100,50,100,200,100,50,100],
    '강수확률':[80,70,90,10,20,30,50,90,20,80,50,10]
})
#print(df)

#print(df.pivot('지역','요일'))
#print(df.pivot('요일','지역'))
#print(df.pivot('요일','지역','강수량'))

# 중복 허용 후 호출은 오류...
#print(df.pivot('지역','요일'))

# pivot_table 중복 데이터 처리
#print(pd.pivot_table(df,index='요일',columns='지역', aggfunc=np.mean))

new_df = df.set_index(['지역','요일'])
#print(new_df)

#print(new_df.unstack(0).stack(0))
#print(new_df.unstack(0).stack(1))

df1 = pd.DataFrame({'key1':np.arange(10), 'value1':np.random.randn(10)})
df2 = pd.DataFrame({'key1':np.arange(10), 'value1':np.random.randn(10)})
df3 = pd.DataFrame({'key2':np.arange(10), 'value2':np.random.randn(10)})

#print(pd.concat([df1,df2]))     # concat 행으로 결합하고, 인덱스도 그대로 붙는다
#print(pd.concat([df1,df2],ignore_index=True)) # 인덱스 무시하고 다시 인덱스 세팅

#print(pd.concat([df1,df2],axis=1))  # axis = 1 열 레벨로 붙는다

customer = pd.DataFrame({'customer_id':np.arange(6), 
                            'name':['철수','영희','길동','영수','수민','동건'], 
                            '나이':[40,20,21,30,31,18]})
orders = pd.DataFrame({'customer_id':[1,1,2,2,2,3,3,1,4,9], 
                            'item':['치약','칫솔','이어폰','헤드셋','수건','생수','수건','치약','생수','케이스'], 
                            'quantity':[1,2,1,1,3,2,2,3,2,1]})

#print(customer)
#print(orders)

#print(pd.merge(customer, orders, on='customer_id', how='inner'))       # inner join
#print(pd.merge(customer, orders, on='customer_id', how='left'))        # left outer join 
#print(pd.merge(customer, orders, on='customer_id', how='right'))       # right outer join

cust1 = customer.set_index('customer_id')
order1 = orders.set_index('customer_id')

#print(cust1)
#print(order1)

#print(pd.merge(cust1, order1, left_index=True, right_index=True))      # left index랑 right index랑 join

print(pd.merge(customer, orders, on='customer_id').groupby('item').sum().sort_values(by='quantity', ascending=False))
print(pd.merge(customer, orders, on='customer_id').groupby(['name','item']).sum().loc['영희'])