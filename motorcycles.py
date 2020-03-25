# Chapter 3
motorcycles = ['honda', 'yamaha', 'suzuki'] # Initial list of motorcycles
print(motorcycles)

motorcycles[0] = 'ducati' # Changes the value of element in list with index of 0
print(motorcycles)

motorcycles.append('honda') # Adds a new element to the list of motorcycles
print(motorcycles)

motorcycles = [] # Creates an empty list of motorcycles
print(motorcycles)

motorcycles.append('honda') # Appends Honda
motorcycles.append('yamaha') # Appends Yamaha
motorcycles.append('suzuki') # Appends Suzuki
print(motorcycles)

motorcycles.insert(0, 'ducati') # Inserts a new element into the list at the specified index
print(motorcycles)

del motorcycles[0] # Removes element in the list at index 0
print(motorcycles)

del motorcycles[1] # Removes element in the list at index 1
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] # Initial list of motorcycles
print(motorcycles)

popped_motorcycle = motorcycles.pop() # Pops the last element in the list - assigning it to a variable and then removing it from the list
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] # Initial list of motorcycles
print(motorcycles)

popped_motorcycle = motorcycles.pop(1) # Pops the list element at index of 1
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] # Initial list of motorcycles
print(motorcycles)

motorcycles.remove('ducati') # Removes first occurrence of list element with value of 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] # Initial list of motorcycles
print(motorcycles)

too_expensive = 'ducati' # Set variable to motorcycle which is too expensive
motorcycles.remove(too_expensive) # Removes first occurrence expensive motorcycle from list using variable
print(too_expensive)
print(motorcycles)


