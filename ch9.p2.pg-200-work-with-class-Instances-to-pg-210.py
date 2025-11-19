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
		
	

		
		
my_car = Car('audi','a4',2009)
print(my_car.description())
my_car.read_odo()

#Modifying attributes
my_car.odometer = 23
my_car.read_odo()

#Modifying through method
my_car.update_odo(20)
my_car.read_odo()
