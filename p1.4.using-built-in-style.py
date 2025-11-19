import matplotlib.pyplot as plt
#print(plt.style.available)

def graph(x,y):
	plt.style.use('dark_background')
	fig,ax = plt.subplots()

	ax.plot(x,y,linewidth=3)
	ax.set_title('Square Numbers',fontsize=20)
	ax.set_xlabel('Value',fontsize=16)
	ax.set_ylabel('Square of value',fontsize=16)

	ax.tick_params(axis='both',labelsize=12)
	
	#ax.set_aspect('equal')#,adjustable='box') Ajaira -_-
	plt.show()

if __name__=='__main__':
	x=[1,2,3,4,5,6,7,8,9]
	y=[1,4,9,16,25,36,49,64,81]

	graph(x,y)
