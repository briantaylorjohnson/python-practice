### Chapter 8: Functions

## Storing Your Functions in Modules

# Importing an Entire Module (Cont'd)

import pizza3 # Imports all functions in module pizza3.py which is in the same directory as this file (making_pizzas.py) -- Must use dot notation

from pizza3 import make_pizza as mp # Imports just the make_pizza function from pizza3.py and creates an alias for the function

import pizza3 as p # Imports all functions in module pizza3.py and creates an alias for the module

# 'from pizza3 import *' can be used to import every function in a module, but this should not be used for larger modules
# The best approach is to import the functions you need, or import the the entire module and use dot notation
# Importing all functions this way can overwrite existing variables or functions, which would likely create errors

pizza3.make_pizza(12, "Cheese", "Bacon", "Pineapple") # Calls make_pizza with import from line 7

print("\n")

p.make_pizza(16, "Cheese", "Pepperoni") # Calls make_pizza in pizza3.py module with alias "p" from line 11

print("\n")

mp(8, "Pesto", "Mozeralla", "Pine nuts") # Calls make_pizza as mp because of the syntax from line 9

print("\n")