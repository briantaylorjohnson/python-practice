### Chapter 10: Files and Exceptions

## Exceptions

# Handling the FileNotFound Error

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        """
        Using variable 'f' is a common convention when opening files
        Encoding argument can be used if system default encoding doesn't match file encoding
        """

        content = f.read()

except FileNotFoundError:
    print(f'The file {filename} which you tried to open does not exist.')

# Analyzing Text 

else:
    # Count the approximate number of words in the file.

    words = content.split()

    num_words = len(words)

    print(f'The file {filename} has about {num_words} words.')