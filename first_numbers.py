# Chapter 4

for value in range(1, 5): # The range function makes it easy to generate a series of numbers -- look and see that 5 is not included! 
	print(value)

print("\n") # New line

for value in range(5): # If only one argument is passed in the range() function, then it starts at 0
	print(value)

print("\n") # New line

# Using range() function to create a list of numbers with list() function
numbers = list(range(1,6))
print(numbers)

