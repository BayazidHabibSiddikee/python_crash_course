import matplotlib.pyplot as plt
from random import randint as rn
x=range(1,1001)
y=[i**2 for i in x]
color =[rn(1,100) for _ in range(len(x))]

plt.style.use('dark_background')
fig , ax = plt.subplots()
ax.scatter(x,y,s=50,c=color,cmap='viridis')

ax.axis([0,1000,0,1000**2])
plt.show()
