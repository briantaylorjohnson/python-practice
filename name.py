# Chapter 2
name = "ada lovelace"
print(name.title()) # Title case
print(name.upper()) # Upper case
print(name.lower()) # Lower case

first_name = "tom"
last_name = "thumb"
full_name = f"{first_name} {last_name}" # F-strings
print(full_name.title())
print(f"Hello there, {full_name.title()}!") # F-strings in print function

message = f"My name is {name.title()}." # F-strings in variable
print(message)

print("Python")
print("\tPython") # Adding a tab
print("\nPython\n") # Adding a new line

print("Languages:\nPython\nC\nJavaScript\n") # Adding new lines

print("Languages:\n\tPython\n\tC\n\tJavaScript\n") # Adding new lines and tabs

favorite_language = "Python " # Whitespace on right side
print(favorite_language)
print(favorite_language.rstrip()) # Whitespace on right side stripped in output

favorite_language = favorite_language.rstrip() # Whitespace on right side stripped in variable
print(favorite_language)

favorite_language = "  Python3  " # Whitespace on both sides
print(favorite_language.rstrip()) # Whitespace on right side stripped
print(favorite_language.lstrip()) # Whitespace on left side stripped
print(favorite_language.strip()) # Whitespace on both sides stripped

print("\n\n")

addition = 2 + 3 # Addition
print(addition)

subtraction = 2 - 3 # Subtraction
print(subtraction)

multiplication = 9 * 9 # Multiplication
print(multiplication)

division = 9 / 4 # Division
print(division)

exponents = 9 ** 2 # Exponents
print(exponents)

exponents = 9 ** 3 # Exponents
print(exponents)

order_of_ops = ((9 * 8) / 2) ** 2 # Order of Operations
print(order_of_ops)

floats = 0.2 + 0.1 # Watch out for floats and lots of decimal places
print(floats)

universe_age = 14_000_000_000 # Using underscores to make big numbers more readable
print(universe_age)

x, y, z = 0, 1, 2 # Assigning values to more than one variable in a single line
print(x)
print(y)
print(z)

MAX_CONNECTIONS = 5000 # Using all caps to indicate a constant in Python is a common practice
print(MAX_CONNECTIONS)

import this # Displays "The Zen of Python" by Tim Peters
