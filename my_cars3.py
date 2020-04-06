### Chapter 9: Classes

## Importing Classes

# Importing a Module into a Module (Cont'd)

from car import Car
from electric_car2 import ElectricCar

from electric_car2 import ElectricCar as EC # Imports ElectricCar class from electric_car2.py with alias EC

my_beetle = Car('volkswagon', 'beetle', 1978)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'type s', 2021)
print(my_tesla.get_descriptive_name())

my_tesla2 = EC('tesla', 'type s', 2017)
print(my_tesla2.get_descriptive_name())