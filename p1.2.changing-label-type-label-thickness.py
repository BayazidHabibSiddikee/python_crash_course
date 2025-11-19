
import matplotlib.pyplot as plt
y = [1,4,9,16,25]
fig , ax = plt.subplots()
ax.plot(y,linewidth=3)

ax.set_title('Square Number',fontsize=24)
ax.set_xlabel("Value",fontsize=11)
ax.set_ylabel('Square of value')#default maybe 11/10

ax.tick_params(axis='both',labelsize=20)

plt.show()

