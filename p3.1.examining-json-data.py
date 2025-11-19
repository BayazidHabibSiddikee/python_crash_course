import json

file = 'eq_data/eq_data_1_day_m1.geojson'
with open(file) as f:
    data = json.load(f)


all_eq = data['features']
print(len(all_eq)) #Number of occured earth quakes

#Extracting magnitude
mag , lons ,lats  =[],[],[]
for i in all_eq:
    m = i['properties']['mag']
    mag.append(m)
    lons.append(i['geometry']['coordinates'][0])
    lats.append(i['geometry']['coordinates'][1])
    
print(mag[:10])
print(lons[:5])
print(lats[:5])


'''
rb = 'data/readable_eq_data.geojson'
with open(rb,'w') as f:
    json.dump(data,f,indent=4)
'''

