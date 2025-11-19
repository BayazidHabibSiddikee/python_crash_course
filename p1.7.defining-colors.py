import matplotlib.pyplot as plt
from random import randint as rn
x=range(1,1001)
y=[i**2 for i in x]
color =[rn(1,100) for _ in range(len(x))]

plt.style.use('dark_background')
fig , ax = plt.subplots()

ax.set_title('Square value table',fontsize=24,color='skyblue')
ax.set_xlabel('Value',fontsize=16,color='skyblue')
ax.set_ylabel('Square of value',fontsize=16,color='skyblue')


#ax.scatter(x,y,s=10,c=x,cmap=plt.cm.Reds)
ax.scatter(x,y,s=10,c=color,cmap=plt.cm.Blues)

ax.axis([0,1000,0,1000**2])
plt.show()

plt.savefig('p1.7.figure.png',bbox_inches='tight')
