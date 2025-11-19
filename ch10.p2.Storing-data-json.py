import json
'''
num =[1,2,3,4,6,4,7,9]
with open('number.json','w') as a:
	json.dump(num,a)''' #Fist created a number.json file now I will open that by another function of json
	

with open('number.json') as b:
	data =json.load(b)
	print(data)
