### Chapter 8: Functions

## Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
    """ Print the list of toppings that have been requested. """
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "extra cheese", "anchovies")


def make_pizza(*toppings):
    """ Summarize the pizza we are about to make. """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("mozerella")
make_pizza("green peppers", "tomatoes", "bacon")


## Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    """ Summarize the pizza we are about to make. """
    print(f"\nMaking {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra, extra cheese')

