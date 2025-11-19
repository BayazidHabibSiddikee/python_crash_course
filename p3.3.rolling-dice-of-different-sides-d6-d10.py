from plotly.graph_objs import Bar, Layout
from  plotly import offline
from random import choice
from die import Die

die1 = Die(6)
die2 = Die(10)

result=[]
for i in range(10000):
    f = die1.roll() + die2.roll()
    result.append(f)

x_val = list(range(2, die1.num + die2.num + 1 ))
frequency =[result.count(r) for r in x_val]

data = [Bar(x=x_val,y=frequency)]

layout = Layout(title='Results of two rolling dice of D6 and D10 10k times',xaxis={'title':'Result','dtick':1}, yaxis={'title':'Frequency'})

offline.plot({'data':data,'layout':layout},filename='p3.3.two-rolling-dice-of-different-size.html')


