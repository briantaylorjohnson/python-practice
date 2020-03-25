# Chapter 4

# Tuples -- look like lists except they use parentheses instead of square brackets

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# If you try to change the elements in a tuple, an error will be thrown
# Also note that tuple with a single element will need to have a trailing comma when it is instantiated

print("\n") # New line

# Looping through a tuple
for dimension in dimensions:
	print(dimension)

print("\n") # New line

# While you can't change a tuple, you can overwrite a variable that is assigned the value of a tuple

print("Original Dimensions:")

for dimension in dimensions:
	print(dimension)

print("\n")

print("New Dimensions:")

dimensions = (400, 100)

for dimension in dimensions:
	print(dimension)

