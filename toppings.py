### Chapter 5

## Checking for Inequality

# Set value of requested_topping
requested_topping = 'mushrooms'

# IF Statement Checking Inequality
if requested_topping != 'anchovies':
    print("Hold the anchovies, boss!")


## Numerical Comparison

age = 18 # Sets age to 18
print(age == 18) # Checks if age is not equal to 18 and prints out the results (True)
print(age !=18) # Checks if age is not equal to 18 and prints out the results (False)

print(age > 10) # Greater than (True)
print(age < 10) # Less than (False)
print(age >= 11) # Greater than or equal to (True)
print(age <= 10) # Less than or equal to (False)


## Checking Multiple Conditions

age_0 = 2 # Set age_0 to 2
age_1 = 4 # Set age_1 to 4

# Using AND
print(age_0 >= 1 and age_1 >=5) # Checks if age_0 is greater than or equal to 1 AND if age_1 is greater than or equal to 5, then prints the result (False)

#Using OR
print(age_0 >= 2 or age_1 > 10) # Checks if age_0 is greater than or equal to 2 OR if age_1 is greater than 10, then prints the result (True)
print(age_0 > 3 or age_1 > 4) # Checks if age_0 is greater than 3 OR age_1 is greater 4, then prints the result (False)


## Checking Whether a Value is in a List

# Initial List
requested_toppings = ['mushrooms', 'pepperonis', 'onions', 'pineapple']

# In List?
print('ham' in requested_toppings) # Checks to see if 'ham' is in requested_toppings list and prints the result (False)
print('pineapple' in requested_toppings) # Checks to see if 'pineapple' is in request_toppings list and prints the result (True)









