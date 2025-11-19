import csv

file='weather_data/sitka_weather_07-2021_simple.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
