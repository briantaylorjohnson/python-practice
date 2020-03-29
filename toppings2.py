### Chapter 5

## IF Statements

# Checking Multiple IF Statements
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms for you, sir...')

if 'pepperonis' in requested_toppings:
    print('Adding pepperonis for you, sir...')

if 'extra cheese' in requested_toppings:
    print('Adding extra cheese for you, sir...')

print('Finished making your pizza! Voila!\n')


## Using IF Statements with Lists

# Checking for Special Items
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Oh no, I'm sorry. We are out of {requested_topping}.")
    else:
        print(f'Adding {requested_topping}...')

print('Finished making your pizza. Voila!\n') 

# Checking If a List is Empty
empty_request = []

if empty_request:
    for requested_topping in empty_request:
        print(f'Adding {requested_topping}...')

else:
    print('Are you sure you want a plain pizza?\n')


# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}... Smells so good!')

    else:
        print(f'Sorry! We are out of {requested_topping}. Try again another day."')

print('Finished making your pizza!')


