class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # default

    def description(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def update_odo(self, x):  # modifying through method
        if x >= self.odometer:
            self.odometer = x
        else:
            print("You can't roll back an odometer!")

    def increment(self, miles):
        self.odometer += miles

    def read_odo(self):  # For default
        print(f"This car has reading {self.odometer} miles.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 200  # default assumption
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
