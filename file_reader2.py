### Chapter 10: Files and Exceptions

## Reading from a File

# Reading Line by Line

filename = 'pi_digits.txt'

print('Reading line by line:')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('')

# Making a List of Lines from a File

print('Making a list of lines from a file:')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
