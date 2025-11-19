'''
a = open('car.py','r')
b = a.read()
print(b)

with open('car.py') as obj:
	contents = obj.read()
	print(contents)
print(contents)
'''

with open('car.py') as obj:
	for i in obj:
		print(i)
