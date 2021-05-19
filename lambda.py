import functools

# sort by lambda
a = ['galio','nunu','lux','vayne','kassadin','teemo','blitzcrank']
a.sort()
print(a)

a.sort(key=lambda x:len(x))
print(a)

# filter by lambda
num = [1,2,3,6,8,9,10,11,13,15]
print(num)
print(list(filter(lambda x : x%2 == 0,num)))

print(list(map(lambda x:x**2, num)))

# reduce by lambda
b = [1,3,5,8]
print(b)

print(functools.reduce(lambda x,y: x+y,b))