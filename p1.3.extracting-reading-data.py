import csv
file=('weather_data/sitka_weather_07-2021_simple.csv')
#with open(file) as f:
'''
f = csv.reader(file)

f_h = next(f)
print(f_h)

#print(f)
for i in f:    
    print(i[1])
    
file.close() '''

with open(file) as f:
    a = csv.reader(f)
    
    f_h = next(a)
    print(f_h)
    
    for i,j in enumerate(f_h):
        print(i,j)
    
    data =[]
    for i in a:
        b = i[5]
        print(b)
        data.append(b)
print(data)
