### Chapter 9: Classes

## Importing Classes

# Importing a Single Class (Cont'd)

from car2 import Car # Imports the Car class from car2.py in the same directory

my_new_car = Car('chevrolet', 'silverado', '2020') # Creates new instance of Car from car2.py for my new car
print(my_new_car.get_descriptive_name()) # Calls the get_descriptive_name() method from in Car class imported from car2.py for the instance of my new car

my_new_car.odometer_reading = 23 # Sets the odometer reading of my_new_car instance of Car class imported from car2.py
my_new_car.read_odometer()  # Calls the read_odometer() method from Car Class imported from car2.py for the instance of my new car
