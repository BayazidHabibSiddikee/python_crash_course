import json
def greet():
	filename  = 'username.json'
	try:
		with open(filename) as f:
			user = json.load(f)
	except FileNotFoundError:
		user = input("What's your name?\n:")
		with open(filename,'w') as f:
			user = json.dump(user,f)
			print(f'We will remember you')
	else:
		print('Welcome back sir '+user)
greet()
