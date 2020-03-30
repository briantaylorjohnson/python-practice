### Chapter 6

## Working with Dictionaries (Cont'd)

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points']) -- This would throw an error because points does not exist in the dictionary; consider using get() instead of square bracket notation

point_value = alien_0.get('points') # Returns none because points does not exist in the dictionary
print(point_value)

point_value = alien_0.get('points', '\nNo point value assigned') # The second argument in the get() method allows a message to be returned instead of none
print(point_value)

