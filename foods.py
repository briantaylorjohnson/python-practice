# Chapter 4

# Copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:] # Copies my_foods list to friend_foods variable

print("My favorite foods are:")
print(my_foods)

print("\n") # New line

print("My friend's favorite foods are:")
print(friend_foods)

print("\n") # New line

# Append new foods to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n") # New line

print("My friend's favorite foods are:")
print(friend_foods)