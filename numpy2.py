#08/05/26 - numpy is python library used for numbers and arrays - can handle lists well

import numpy as np, random


#regular array + operators
a = np.array([0,1,2,3,15,20,7,43,68,100])
print(a)

print(a+5)
print(a**10)

#empty array
b = np.array([])
print(b)

#arrays of zero
c = np.zeros(5)
d = np.zeros((3,3))
print(c,d)

#arrays of ones
c = np.ones(5)
d = np.ones((3,3))
print(c,d)


print(a[0:])
print(a[1:5])
print(a[0:-1:2])
print(a<5)
print(a[a<5])
print(a[a%5==0])
#rnadom permuatation
e = np.random.permutation(np.arange(20))

print(e)

e = np.random.permutation(np.arange(20).reshape(4,5))

print(e)

print(a[(a>5) & (a<50)])

