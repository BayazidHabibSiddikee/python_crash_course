import matplotlib.pyplot as plt
from random import randint as rn

def graph(x,y):
	color = [rn(1,100) for _ in range(len(x))]
	plt.style.use('dark_background')
	fig,ax = plt.subplots()
	ax.scatter(x,y,s=50,c=color,cmap='viridis')
	
	ax.tick_params(axis='both',which='major',labelsize=14)
	plt.show()

if __name__=='__main__':
	x=[]
	y=[]
	for _ in range(100):
		x.append(rn(1,200))
		y.append(rn(1,200))
	graph(x,y)
