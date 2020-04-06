### Chapter 9: Classes

## Importing Classes

# Importing Multiple Classes from a Module

from car3 import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 1978)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())