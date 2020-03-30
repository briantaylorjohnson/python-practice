### Chapter 6

## Nesting

# A List in a Dictionary

# Store information of the pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

# Summarize the order
print(f'You ordered a {pizza["crust"]} crust pizza with the following toppings:')

for topping in pizza['toppings']:
    print(f'\t{topping}')
