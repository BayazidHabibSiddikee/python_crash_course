import csv
import matplotlib.pyplot as plt
from datetime import datetime

file=('weather_data/sitka_weather_07-2021_simple.csv')
with open(file) as f:
    a = csv.reader(f)
    b = next(a) #U'll be fucked up if u don't give
    data,dates =[],[]
    for i in a:
        data.append(i[5])
        #print(i[2])
        dates.append(datetime.strptime(i[2],'%Y-%m-%d'))


print(dates)


#Let's plot the data
plt.style.use('dark_background')
fig,ax =plt.subplots(figsize=(10,6))
ax.plot(dates,data,c='skyblue',linewidth=3)

ax.set_title('Daily high temperature, July 2021',fontsize=24)
plt.xlabel('Dates',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)',fontsize=16)

plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

