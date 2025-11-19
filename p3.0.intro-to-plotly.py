
'''
from plotly.graph_objs import Bar,Layout
from plotly import offline

x_val = [1,2,3,4,5,6]
y_val  = [15,22,10,18,13,20]

data = [Bar(x=x_val,y=y_val)]

x_axis = {'title':'Result'}
y_axis = {'title':'Frequency of result'}

my_layout = Layout(title='Result of rolling dice',xaxis=x_axis,yaxis=y_axis)

offline.plot({'data':data,'layout':my_layout},filename='d6.html')
'''



#A short form of this 
from plotly.graph_objs import Bar, Layout
from  plotly import offline

data = [Bar(x=[1,2,3,4,5],y=[10,15,20,15,10])]
my_layout = Layout(title = 'Bar chart of a rolling dice',xaxis={'title':'Result'},yaxis={'title':'Frequency'})

offline.plot({'data':data,'layout':my_layout},filename='p1.0.html')

