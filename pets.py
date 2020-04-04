### Chapter 7

## Using while loops with Lists and Dictionaries

# Removing all instances of specific values from a list

pets = ['dog', 'cat', 'gerbil', 'snake', 'cat', 'dog', 'rabbit', 'cat']

iteration = 1

print(pets)

while 'cat' in pets: # While loop iterates until 'cat' is not in the pets list

    pets.remove('cat') # Removes the first instance of 'cat' in the pets list. Each subsequent iteration will remove the next instance of 'cat'.

    iteration += 1

print(f"\nNumber of iterations: {iteration} \n")

print(pets)

