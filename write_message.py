### Chapter 10: Files and Exceptions

## Writing to a File

# Writing to an Empty File

file_name = 'programming.txt'

""" 'w' , 'r' , and 'a' are 'write', 'read only', and 'append' respectively; there is also 'r+' which allows reading and writing to the file. """
with open(file_name, 'w') as file_object:
    file_object.write('I love programming.')


# Writing Multiple Lines

with open(file_name, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')


# Appending to a File

with open(file_name, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
