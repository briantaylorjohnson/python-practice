### Chapter 6

## A Simple Dictionary

# Creates alien_0 dictionary
alien_0 = {'color': 'green', 'points': 5}

# Accessing Values in a Dictionary
print(alien_0['color']) # Accesses the color in alien_0 dictionary
print(alien_0['points']) # Accesses the points in alien_0 dictionary

new_points = alien_0['points'] # Sets variable new_points to points in alien_0 dictionary

print(f'\nYou just earned {new_points} points!\n') # Uses F-string to print message with new_points variable

# Adding New Key-Value Pairs
print(alien_0)
print('\n')

alien_0['x_position'] = 0 # Creates a new key-value pair in alien_0 for x_position
alien_0['y_position'] = 25 # Creates a new key-value pair in alien_0 for y_position

print(alien_0)
print('\n')

# Starting with an Empty Dictionary
alien_0 = {}

print(alien_0)
print('\n')

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print('\n')

# Modifying Values in a Dictionary
print(f'The alien is {alien_0["color"]}.\n')

alien_0['color'] = 'yellow'

print(f'The alien is now {alien_0["color"]}!\n')

# More Complex Sample
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position of alien: {alien_0["x_position"]}.')

if alien_0['speed'] == 'slow': # Moves alient to the right 1 unit
    x_increment = 1

elif alien_0['speed'] == 'medium': # Moves alient to the right 2 units
    x_increment = 2

else: # Moves alient to the right 3 units
    # This must be a fast alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment # Calculates new position

print(f'New position of alien: {alien_0["x_position"]}.\n')

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] # Removes the points key-value pair from alien_0
print(alien_0)






