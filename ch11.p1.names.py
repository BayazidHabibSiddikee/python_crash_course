from name_function import get_name as GN
print("Enter q or ctrl c to quit")
try:
	while True:
		first=input("Enter first name: ")
		if first == 'q':
			break
		last = input("Enter last name: ")
		if last == 'q': #Double check -_-
			break
		name = GN(first,last)
		print(f'Neatly formatted name: {name}')
except Exception as e:
	print('Done')
