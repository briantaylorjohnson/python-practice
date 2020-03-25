# Chapter 4

# Use range() and list() functions to produce the first 10 squares 

squares = [] # Squares list

for value in range(1,11): # For loop for numbers 1 through 10
	square = value ** 2 # Calculates the square of the value
	squares.append(square) # Appends the squared value to the squares list

print(squares) # Prints the full squares list

print("\n") # New line

# Simple Statistics (MIN, MAX, SUM)

digits = list(range(10))
print(digits)
print("\n")

print("Minimum:")
print(min(digits))
print("\n")

print("Maximum:")
print(max(digits))
print("\n")

print("Sum:")
print(sum(digits))
print("\n")


# List Comprehension -- a more concise way to generate a list

squares = [value**2 for value in range(1, 11)] # Generates a list where each value in the range() function is squared and the squared value is added to the list
print(squares)

