import numpy as np
import matplotlib.pyplot as plt

# 기본적인 선 그래프
# x = np.linspace(0,10,11)
# y = x**2 + x + 2 + np.random.randn(11)

# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('X-Y relation')
# plt.grid(True)
# plt.xlim(0,20)
# plt.ylim(0,200)

# plt.subplot(2,2,1)
# plt.plot(x,y,'r')

# plt.subplot(2,2,2)
# plt.plot(x,y,'g')

# plt.subplot(2,2,3)
# plt.plot(y,x,'k')

# plt.subplot(2,2,4)
# plt.plot(x,np.exp(x),'b')

# plt.show()

# hist 함수
#data = np.random.randint(1,100, size=200)
#plt.hist(data,bins=10)
#plt.xlabel('값')
#plt.ylabel('개수')
#plt.grid(True)
#plt.show()

#print(np.random.choice(np.arange(1,46), size=6), replace=False) # replace=False는 비복원 추출이기때문에 중복값이 나올 수 없다


# PI 근사치 구하기
# PI / 4 : 1 = 4분원에 찍힌 점 개수: 전체 시도 횟수
# 4분원에 찍힌 점 개수 = PI / 4 * 전체 시도 횟수
# PI = 4 * 4분원에 찍힌 점 개수 / 전체 시도 횟수
# x**2 + y**2 < 1 이 원 안에 있는 점
total = int(1e7)

points = np.random.rand(total,2)
print(np.sum(np.sum(points**2,axis=1) < 1))
print(4 * np.sum(np.sum(points**2,axis=1) < 1) / total)