from car import Car
my_car = Car('audi','a4',2019)
print(my_car.description())

my_car.update_odo(23)
my_car.read_odo()


from car import ElectricCar
tesla = ElectricCar('tesla','model a',2013)
print(tesla.description())
tesla.battery.describe_battery()


#Importing whole
import car
a = car.Car('volkswagen','beetle',2019)
print(a.description())


