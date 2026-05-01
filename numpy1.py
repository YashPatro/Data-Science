import numpy as np, random

l = [random.randint(0,20) for i in range(10)]
print(l)


for i,v in enumerate(l):
    v*=2
    l[i] = v

print(l)

#second method create data 

l1 = list(range(1,21,2))
print(l1)

arr = np.array(range(1,21,2))
print(arr)
l2 = l1*2
arr2 = arr*2
print(l2)
print(arr2)
l3 = l1+l1
arr3 = arr+arr
print(l3)
print(arr3)

# create arrays with different shpes 
a = np.zeros((5,5))
b = np.ones((3,3))
c = np.arange(20).reshape(4,5)
print(a,b,c)