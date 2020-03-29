### Chapter 2

## Simple IF Statement

# Initial List
cars = ['audi', 'bmw', 'subaru', 'toyota']

# FOR Loop
for car in cars:

# IF Statement
	if car == 'bmw':
		print(car.upper())

	else:
		print(car.title())

## Conditional Tests

# Equality
 
car = 'bmw' # Sets value of car
print(car == 'bmw') # Checks if the value of car is equal to 'bmw' and prints out the result (True)
print(car == 'audi') # Checks if the value of car is equal to 'audi' and prints out the result (False) 

# Ignoring Case When Checking Equality

car = 'Audi' # Sets value of car
print(car == 'audi') # Checks if the value of car is equal to 'audi' and prints out the result (False)
print(car.lower() == 'audi') # Sets car to all lower case, checks if the value of car is equal to 'audi', and prints out the result (True)
print(car) # Value of car is still lower case






