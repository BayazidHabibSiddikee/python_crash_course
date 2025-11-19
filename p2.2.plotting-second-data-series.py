import csv
from datetime import datetime as dt
import matplotlib.pyplot as plt

file = 'weather_data/sitka_weather_2021_simple.csv'
with open(file) as f:
    a = csv.reader(f)
    b = next(a)
    
    dates, high, low =[],[],[] #For both high and low temperature
    for i in a:
        high.append(int(i[4]))
        low.append(int(i[5]))
        dates.append(dt.strptime(i[2],'%Y-%m-%d'))

plt.style.use('dark_background')#'classic')#'dark_background')
fig,ax = plt.subplots(figsize=(10,6))

ax.plot(dates,high,c='blue',linewidth=2,alpha=0.5) #To shade
ax.plot(dates,low,c='red',linewidth=2,alpha=0.5)
plt.fill_between(dates,high,low,facecolor='blue',alpha=0.3)

plt.title('Daily high and low temperature-2021',fontsize=24)
ax.set_xlabel('Dates',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()   
