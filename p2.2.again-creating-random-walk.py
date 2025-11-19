import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self,num = 5000): #5k steps would take
        self.num = num
        self.x_val = [0]
        self.y_val = [0] #always start from 0,0
    
    def direction(self):
        while len(self.x_val)<self.num:
            x_dir = choice([1,-1])
            x_dis = choice([0,1,2,3,4])
            x_step = x_dir * x_dis
            
            y_dir = choice([1,-1])
            y_dis = choice([0,1,2,3,4])
            y_step = y_dir * y_dis
            
            #Reject moves that goes nowhere
            if x_step==0 and y_step==0:
                continue
                
            #Calculate the new position
            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step
            
            
            self.x_val.append(x)
            self.y_val.append(y)
      
      
      
          
while True:
    rw = RandomWalk(50000)
    rw.direction()

    #plt.style.use('dark_background')
    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(10,6),dpi=128)
    ax.scatter(rw.x_val,rw.y_val,s=5,c=rw.y_val,cmap=plt.cm.Blues,edgecolors='none')
    #let's mark starting and ending point
    ax.scatter(rw.x_val[0] , rw.y_val[0], s=50, c='red',edgecolors='none')
    ax.scatter(rw.x_val[-1],rw.y_val[-1],s=50,c='green',edgecolors='none')
    
    #cleaning up the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    
    plt.show()
    
    run =input("Make another? 'y' or quit 'q'")
    if run=='q':
        break
