### Chapter 9: Classes

## Importing Classes

# Importing an Entire Module

import car3

my_beetle = car3.Car('volkswagon', 'beetle', 1978)
print(my_beetle.get_descriptive_name())

my_tesla = car3.ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())