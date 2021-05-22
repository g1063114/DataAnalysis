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

print(np.random.uniform(1.0,3.0, size=(4,5)))
