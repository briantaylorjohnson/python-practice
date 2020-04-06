### Chapter 9: Classes

## Importing Classes

# Storing Multiple Classes in a Method (Cont'd)

from car3 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', '2020')

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

my_tesla.battery.get_range()