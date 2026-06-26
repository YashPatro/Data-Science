import matplotlib.pyplot as plt
import numpy as np 
x = [0,12,14,15,20,72]
y = [1,13,17,18,30,56]
plt.plot(x,y)
plt.show()


#formatting and adding it 

plt.plot(x,y,'g^')
plt.show()

#setting tht limit - the number on each axis 

plt.plot(x,y)
plt.axis([0,100,0,75])
plt.show()

#adding the label legend line widths and the title 
plt.plot(x,y,'g-',label = 'y = x',linewidth = 4)
plt.axis([0,100,0,75])
plt.xlabel('x (seconds)')
plt.ylabel('y (distance)')
plt.legend()
plt.title('x vs y')
plt.show()

#plotting mutple graphs on a single plot
m = [4,20,22,30,51,63]
n = [10,20,30,40,50,60]

plt.plot(x,y,'b--',label = 'y = x**2',linewidth = 5)
plt.plot(x,m,'g-',label = 'y = x**3',linewidth = 5)
plt.axis([0,100,0,75])
plt.xlabel('x (seconds)')
plt.ylabel('y (distance)')
plt.legend()
plt.title('x vs y')
plt.show()
x = np.arange(0,10,0.2)
print(x)
y1 = x**2
y2 = x**3
plt.plot(x,y1,'g--',x,y2,'b-')

plt.show()

plt.bar(m,n,color = 'b')
plt.bar(n,y,color = 'r')
plt.show()

#hw

x = np.arange(-5, 5, 0.1)

y = x
z = x**2
a = x**3

plt.plot(x, y, 'g-', label='y = x')
plt.plot(x, z, 'b--', label='y = x**2')
plt.plot(x, a, 'r:', label='y = x**3', linewidth=4)

plt.axis([-10, 10, -10, 10])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Quadratic and Cubic Graphs')
plt.legend()

plt.show()