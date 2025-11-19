import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self,num=5000):
        self.num = num
        
        #Walk starting from 0,0
        self.x_val = [0]
        self.y_val = [0]
        
    def path(self):
        for _ in range(self.num):
            left_right = [-1,1] #if u remove -1 it will go only right
            up_down = [1,-1] #only up , so it won't be random but it awesome to see this shit
            
            x_dir = choice(left_right) # -1
            y_dir = choice(up_down)
            
            distance = [0,1,2,3,4,5,6,7,8,9] #Let's highest be 5 and lowest be None
            x_dis = choice(distance) #4
            y_dis = choice(distance)
            
            x_step = x_dir * x_dis #-4
            y_step = y_dir * y_dis
            
            #Skip if u don't move
            if x_step == 0 and y_step == 0:
                continue
            
            #new steps = 0-4 = -4
            x=self.x_val[-1] + x_step
            y=self.y_val[-1] + y_step
            
            #Appending to the list x_val = [0,-4....]
            self.x_val.append(x)
            self.y_val.append(y)
            
    def show(self):
        for i in range(len(self.x_val)):
            
            print(f"(x,y)=({self.x_val[i]},{self.y_val[i]}) {'x' if self.x_val[i]==self.y_val[i] else ''}")
        
rw = RandomWalk(10000)
rw.path()
rw.show()

plt.style.use('classic')
fig , ax = plt.subplots()
ax.scatter(rw.x_val,rw.y_val,s=15,c=rw.y_val,cmap=plt.cm.Blues,edgecolors='none')

plt.show()     

plt.savefig('p2.1.Random_picture.png',bbox_inches='tight')      
