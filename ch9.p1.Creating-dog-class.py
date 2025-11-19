class Dog:
	def __init__(self,name,age):
		self.name =name
		self.age = age
	def sit(self):
		print(f'{self.name} is now setting')
	def roll(self):
		print(f'{self.name} has rolled over')

my_dog=Dog('Willie',6)
my_dog.sit()
print(f'My dog name is {my_dog.name}')
