### Chapter 10: Files and Exceptions

## Exceptions

# Working with Multiple Files

def count_words(filename):

    """ Count the approximate number of words in a file. """

    try:
        with open(filename, encoding='utf-8') as f:
            """
            Using variable 'f' is a common convention when opening files
            Encoding argument can be used if system default encoding doesn't match file encoding
            """

            content = f.read()

    except FileNotFoundError:
        pass # Use 'pass' to fail silently without any output or exception thrown

    else:
        """ Count the approximate number of words in a file. """

        words = content.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filename = 'alice.txt'

print('Counting the words in a single file: ')
count_words(filename)

print('')

print('Count the words in all the files within a list: ')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)