class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0 #default
		
	def description(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
		
	def update_odo(self,x): #modifying through method
		self.odometer = x
		
	def read_odo(self): #For deafult
		print(f"This car has reading {self.odometer}")

class Battery:  #Instances as attribute
	def __init__(self,b_size = 75):
		self.b_size = b_size
	def d_battery(self):
		print(f'This car has a battery life of {self.b_size}')
		
class Electrical(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()		

my_tesla= Electrical('tesla','SUV',2017)
print(my_tesla.description())
my_tesla.battery.d_battery()
my_tesla.read_odo()
