### Chapter 8: Functions

## Storing Your Functions in Modules

# Importing an Entire Module

def make_pizza(size, *toppings):
    
    """ Summarize the pizza we are about to make. """
    print(f"Making a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"\t- {topping}")

