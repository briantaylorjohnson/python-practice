# Chapter 3
cars = ['bmw', 'audi', 'toyota', 'subaru'] # Initial list of cars
print(cars)

cars.sort() # Sorts elements in list alphabetically -- upper and lower case are different!
print(cars)

cars.sort(reverse=True) # Sorts elements in reverse alphabetically -- upper and lower case are different!
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru'] # Initial list of cars
print("\nHere is the original list of cars:")
print(cars)

print("\nHere is the sorted list of cars:")
print(sorted(cars)) # This sorts the list of cars temporarily

print("\nHere is the reverse sorted list of cars:")
print(sorted(cars, reverse=True)) # This reverse sorts the list of cars temporarily

print("\nHere is the original list of cars again:")
print(cars)
print("\n")

cars = ['bmw', 'audi', 'toyota', 'subaru'] # Initial list of cars
print(cars)

cars.reverse() # Reverses the order of the elements in the list
print(cars)

print("\nLength of the list of cars:")
print(len(cars)) # Finds the length of the list of cars


