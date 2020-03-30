### Chapter 6

## Nesting

# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5} # Dictionary of alien_0
alien_1 = {'color': 'yellow', 'points': 10} # Dictionary of alien_1
alien_2 = {'color': 'red', 'points': 15} # Dictionary of alien_2

aliens = [alien_0, alien_1, alien_2] # List of dictionaries

for alien in aliens: # Loops through aliens list and prints each dictionary
    print(alien)

# More Realistic Example Creating 30 Aliens

aliens = [] # Empty alien list to start with

for alien_number in range(30): # Sets the number of alients to create -- 30
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} # Creates a new alien dictionary for each iteration of the loop
    aliens.append(new_alien) # Adds the new alien to the aliens list

for alien in aliens[:5]: # Prints the first five aliens
    print(alien)

print('...\n')

print(f'Total number of aliens: {len(aliens)}.\n') # Outputs the length of the aliens list

for alien in aliens[:3]: # Changes the values of the first three aliens in the aliens list if the alien's color is green
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]: # Prints the first five aliens
    print(alien)

print('...\n')

print(f'Total number of aliens: {len(aliens)}.\n') # Outputs the length of the aliens list

for alien in aliens[:1]: # Changes the values of the first alien in the aliens list if the alien's color is green or yellow
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]: # Prints the first five aliens
    print(alien)

print('...\n')

print(f'Total number of aliens: {len(aliens)}.\n') # Outputs the length of the aliens list

