### Chapter 9: Classes

## Inheritance

# The __init__() Method for a Child Class

class Car:

    """ A simple attempt to represent a car. """
    def __init__(self, make, model, year):

        """ Initialize attributes to describe car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Sets a default value for the odometer reading

    def get_descriptive_name(self):

        """ Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):

        """ Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):

        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        """ Add the given amount to the odometer reading """
        self.odometer_reading += miles

class Battery:

    """ A simple attempt to model a battery for an electric car. """
    def __init__(self, battery_size=100):

        """ Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):

        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):

        """ Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260

        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):

    """ Represent aspects of a car, specific to an electric vehicle. """
    def __init__(self, make, model, year):

        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # Creates an instance of Battery() within an ElectricCar() instance when it is created
        self.battery_size = 75

    def describe_battery(self):

        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar("tesla", "model s", 2019)

print(my_tesla.get_descriptive_name())


# Defining Attributes and Methods for the Child Class

my_tesla.describe_battery() # Calls the child class describe_battery()) method using the child class attribute battery_size


# Instances as Attributes

my_tesla.battery.describe_battery() # Calls the describe_battery() method within the Battery() instance of the ElectricCar() instance of my_tesla
my_tesla.battery.get_range() # Calls the get_range() method within the Battery()) instance of the ElectricCar() instance of my_tesla





