### Chapter 10: Files and Exceptions

## Reading from a File

# Reading an Entire File

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())
