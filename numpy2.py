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

#hw
arr = np.arange(1, 21)

print(arr[:5])
print(arr[-5:])
print(arr[::3])
print(arr[::-1])

#2
mat = np.arange(49).reshape(7, 7)

mid = mat[2:5, 2:5]
row = mat[0, :]
col = mat[:, -1]

print("Middle 3x3:")
print(mid)
print("First row:")
print(row)
print("Last column:")
print(col)

#prac3
arr = np.arange(1, 16)

c1 = arr[arr < 8]
c2 = arr[arr >= 10]
c3 = arr[arr % 2 != 0]

print("Values < 8:", c1)
print("Count:", len(c1))

print("Values >= 10:", c2)
print("Count:", len(c2))

print("Odd values:", c3)
print("Count:", len(c3))

#4
lst = list(range(1, 11))
arr = np.arange(1, 11)

for i in range(len(lst)):
    lst[i] += 5

arr = arr + 5
print("List after adding 5:", lst)
print("Array after adding 5:", arr)

arr = arr * 3
print("Array after multiplying by 3:", arr)

arr = arr - 2
print("Array after subtracting 2:", arr)