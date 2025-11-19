from plotly.graph_objs import Bar, Layout
from  plotly import offline
from random import choice
from die import Die

'''
x1_val = list(range(1,7)) #For two dice
x2_val = list(range(1,7))
x_val = x1_val + x2_val
x_val = list(range(1,13))
y_val = [choice(x_val) for _ in range(1000)]
frequency=[y_val.count(r) for r in x_val]



data = [Bar(x = x_val, y = frequency)]
layout = Layout(title='Frequency vs Result for two rolling dice', xaxis = {'title':'Result','dtick':1}, yaxis = {'title':'Frequency of result'})

offline.plot({'data':data,'layout':layout},filename = 'p3.2.two-rolling-dice.html')

'''


die1 = Die()
die2 = Die()

result=[]
for i in range(1000):
    f = die1.roll() + die2.roll()
    result.append(f)

x_val = list(range(2, die1.num + die2.num + 1 ))
frequency =[result.count(r) for r in x_val]

data = [Bar(x=x_val,y=frequency)]

layout = Layout(title='Results of two rolling dice',xaxis={'title':'Result','dtick':1}, yaxis={'title':'Frequency'})

offline.plot({'data':data,'layout':layout},filename='p3.2.two-rolling-dice.html')


