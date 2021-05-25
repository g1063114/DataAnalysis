import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3])
s2 = pd.Series(['a','b','c'])
s3 = pd.Series(np.arange(200))
s4 = pd.Series([1,2,3],['a','b','c'])
#print(s1)
#print(s2)
#print(s3)
#print(s4)

#print(s4.index)
#print(s4.values)
#print(s4['a']) 

s = pd.Series([1,1,2,1,2,2,2,1,1,3,4,3,5,5,5,7,np.NaN])
#print(len(s))
#print(s.unique()) # 중복 제거하고 데이터
#print(s.count())   # Nan 데이터 제외한 갯수

a = np.array([2,2,2,2,np.NaN])
#print(a.mean())

b = pd.Series(a)
#print(b.mean())

#print(s.value_counts()) # 값의 빈도

s5 = pd.Series(np.arange(1,11),np.arange(0,10))

s5['a'] = 100

s5.drop('a')                # 복사본 만들어서 결과에서만 'a'인덱스를 지운다... 원본은 그대로
print(s5)                   

s5.drop('a',inplace=True)   # inplace=True는 원본 데이터에서도 삭제... default는 False
print(s5)