import json

from plotly.graph_objs import Scattergeo , Layout
from plotly import offline

file = 'eq_data/eq_data_1_day_m1.geojson'
with open(file) as f:
    a = json.load(f)
data = a['features']

mag,lat,lon=[],[],[]
for i in data:
    mag.append(i['properties']['mag'])
    lat.append(i['geometry']['coordinates'][1])
    lon.append(i['geometry']['coordinates'][0])
    
    
#Map the earth quakes
data =[Scattergeo(lon=lon,lat=lat)]
layout = Layout(title='Global Earthquakes')

offline.plot({'data':data,'layout':layout},filename='global_earthquakes.html')

