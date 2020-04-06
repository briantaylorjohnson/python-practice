### Chapter 10: Files and Exceptions

## Reading from a File (Cont'd)

# Working with a File's Contents

filename = 'pi_digits.txt'

print('Working with a File\'s Contents:')

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip() # strip() method to remove the white space on both sides of each line

print('The strip method removes the white space on both sides of each line in the text file so we have one value for pi.')
print(pi_string)
print(len(pi_string))


# Large Files: One Million Digits

