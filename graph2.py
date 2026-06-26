import matplotlib.pyplot as plt
import random

#stackplot

sleeping = [480,500,390,540,450]
eating = [30,60,75,50,100]
study = [400,360,450,500,300]
scrnTime = [100,200,180,60,20]
actTime = [100,60,180,120,200]
days = [1,2,3,4,5]
plt.plot([],[],color = 'c',label = 'Eating',linewidth = 5)
plt.stackplot(days,sleeping,eating,study,scrnTime,actTime)
plt.legend()
plt.show()


#pie chart
cat = [480,35,450,180,180]
act = ['sleeping','eating','study','screen time','active time']
clrs = ['c','m','r','b','g']
plt.pie(cat,labels = act,colors = clrs,startangle = 90, shadow = True )
plt.title('Piechart')
plt.show()

#histogram
age = [random.randint(1,100) for i in range(20)]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(age,bins,histtype = 'bar' , rwidth  = 0.8)
plt.xlabel('age interval')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()


#scatter grpah
x = [random.randint(0, 10) for i in range(10)]
y = [random.randint(0,10) for i in range(10)]
plt.scatter(x,y,label = 'Scatter Plot',color = 'Red', marker = 'd', s = 100)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()