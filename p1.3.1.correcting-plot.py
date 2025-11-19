import matplotlib.pyplot as plt
y = [1,4,9,16,25]
x = [1,2,3,4,5]
fig , ax = plt.subplots()
ax.plot(x,y,linewidth=3,color='black')

ax.set_title('Square Number',fontsize=24,color='skyblue')
ax.set_xlabel("Value",fontsize=14,color='green')
ax.set_ylabel('Square of value',fontsize=14,color='red')#default maybe 11/10

ax.tick_params(axis='both',labelsize=12)

plt.show()

