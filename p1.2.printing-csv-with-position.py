import csv

file='weather_data/sitka_weather_07-2021_simple.csv'
with open(file) as f:
    a = csv.reader(f)
    h_r = next(a)
    
print(h_r)
for i,j in enumerate(h_r):
    print(i,j)
