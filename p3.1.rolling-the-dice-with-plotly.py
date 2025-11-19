from plotly.graph_objs import Bar,Layout
from plotly import offline
from random import randint


class Die:
    def __init__(self,num=6):
        self.num = num
        
    def roll(self):
        return randint(1,self.num)
        
die=Die()

#Make some roll and store the result in a die
result=[]
for i in range(1000):
    r = die.roll()
    result.append(r)
#print(result)      


#Let's analyze the result
frequency=[]
for i in range(1,die.num+1):
    f = result.count(i) #1 = 175 times 2= 243times etc etc wow 
    #print(f)
    frequency.append(f)
print(frequency)

#Visualize the result
x_val = list(range(1,die.num+1))
data = [Bar(x=x_val, y= frequency)]
print(data)

x_axis = {'title':'Result'}
y_axis = {'title':'Frequency of result'}

my_layout = Layout(title='Results of rolling dice D6 1k times',xaxis = x_axis,yaxis = y_axis)
offline.plot({'data':data,'layout':my_layout},filename = 'd6.html')
