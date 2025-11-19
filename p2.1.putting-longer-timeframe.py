import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = 'weather_data/sitka_weather_2021_simple.csv'
with open(file) as f:
    a = csv.reader(f)
    b = next(a)
    data ,dates = [],[]
    for i in a:
        data.append(int(i[5]))
        dates.append(datetime.strptime(i[2],'%Y-%m-%d'))

plt.style.use('dark_background')
fig,ax=plt.subplots(figsize=(10,6))

ax.plot(dates,data,linewidth=1,c='blue')
plt.title('Daily High Temperature-2021',fontsize=24)
ax.set_xlabel('Dates',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatur(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
