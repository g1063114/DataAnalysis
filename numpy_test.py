import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

#print(np.arange(10))

#print(np.ones((4,5)))

#print(np.ones((2,3,4))) # 3행 4열 행렬 2개 모든 원소 1
#print(np.zeros((2,3)))  # 모든 원소 0

#print(np.eye(5))    # 단위 행렬

#print(np.linspace(1,10,4))  # 1과 10 사이를 4등분

#print(np.random.rand(2,3))  # 0~1 사이 랜덤
#print(np.random.randn(3,4)) # 정규분포
#print(np.random.randint(1,100, size=(3,5)))

#np.random.seed(100)     # 랜덤한 값을 동일하게 다시 생성할때

#x = np.array([1,4,2,8,5,0,3,7,0,4,2,5])
#print(np.random.choice(x, size=(2,2)))

#print(np.random.uniform(1.0,3.0, size=(4,5)))


#temp1 = np.arange(15).reshape(3,5)
#print(temp1.ravel())    # 1차원으로 변경 -> 원본데이터 같이 변경
#print(temp1.ravel(order='C'))   # 행 기준으로 1차원 만듬
#print(temp1.ravel(order='F'))   # 열 기준으로 1차원 만듬

#temp2 = np.arange(15).reshape(3,5)
#print(temp2.flatten())  # 1차원으로 변경 -> 원본데이터 복사해서 복사본 만듬    
#print(temp2.flatten(order='C'))
#print(temp2.flatten(order='F'))

#temp_x = np.arange(15).reshape(3,-1)
#temp_y = np.random.rand(15).reshape(3,-1)

#print(temp_x)
#print(temp_y)

#print(np.add(temp_x,temp_y))
#print(temp_x + temp_y)

#tmp_x = np.arange(15)
#tmp_y = tmp_x.reshape(3,5)
#print(tmp_y)

#print(np.sum(tmp_y, axis=0))    # axis = 0 이면 행 방향으로 연산 진행
#print(np.sum(tmp_y, axis=1))    # axis = 1 이면 열 방향으로 연산 진행

z = np.arange(36).reshape(3,4,3)
#print(z)
#print(np.sum(z, axis=0))        # 3차원 이니까 3개의 행렬이 포개진다고 이해하면 쉬움 z값이 있는것과 동일하게...
#print(np.sum(z, axis=1))
#print(np.sum(z, axis=2))

# 브로드캐스팅 -> 두 ndarray가 다른 shape을 가질 때 shape을 맞춘 후 진행하는 방법
#x = np.arange(12).reshape(4,3)
#y = np.random.rand(3).reshape(1,3)

#print(x+y)

# boolean indexing
#b_x = np.random.randint(10,100, size=20)
#print(b_x)

#mask = b_x % 2 == 0
#print(mask)

#print(b_x[mask])
#print(b_x[b_x % 2 == 0])    # 바로 인덱싱 가능
#print(b_x[b_x > 50])
#print(b_x[(b_x % 2 == 0) & (b_x > 50)])

# Ax = B 형태의 행렬식 구하는 방법
A = np.array([[1,1],[2,4]])
B = np.array([25,64])
print(A)
print(B)

x = np.linalg.solve(A,B)
print(x)
print(np.allclose(A@x,B))   # 행렬 계산이 참인지 확인하는, 행렬의 곱은 @