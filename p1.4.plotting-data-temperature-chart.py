import csv
import matplotlib.pyplot as plt

file=('weather_data/sitka_weather_07-2021_simple.csv')
with open(file) as f:
    a = csv.reader(f)
    
    data =[]
    for i in a:
        data.append(i[5])
print(data)

#plot the temperature graph
plt.style.use('dark_background')
fig , ax = plt.subplots(figsize=(10,6))
ax.plot(data,c ='red',linewidth=2)

plt.title("Daily high temperature , July 2018",fontsize=24)
plt.xlabel('')
ax.set_ylabel('Temperature(f)',fontsize = 16)

plt.tick_params(axis ='both',which='major',labelsize=16)

plt.show()
    
    
