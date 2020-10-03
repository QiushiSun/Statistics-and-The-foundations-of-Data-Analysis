# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

list1=[]
list2=[]

plt.figure()
count=0
n=15000 #做15，000次投掷
left,right=0,1 #约束边界条件
lower,upper=0,1

x=np.random.uniform(left,right,n) #调用均匀分布开始制作点列
y=np.random.uniform(lower,upper,n)

for i in range (0,n-1):
    if(y[i]<=np.log2(x[i]+1)):
        #print(np.log2(x[i]+1))
        list1.append(x[i])
        list2.append(y[i])
        count+=1
        #print (count)
        # 真实值(2ln(2)-1)/ln(2) approx 0.5573
        print('iteration:'+str(i))
        estimation = count / 1.000 / n
        print(estimation)
        print('error:'+str(abs(estimation-0.5573)))

fig=plt.figure()
axes=fig.add_subplot(1,1,1)
axes.plot(list1,list2,'ro',label = "Monte Carlo Method",color='deepskyblue',markersize=0.6)

plt.axis('equal') #防止图形在Jupyter-lab中变形
plt.show()