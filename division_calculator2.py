### Chapter 10: Files and Exceptions

## Exceptions

# Using Exceptions to Prevent Crashes

""" The else Block """

""" This gracefully handles the ZeroDivisionError returned if program tries to divide by zero. """

print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')

while True:
    first_num = input('\nFirst number: ')

    if first_num == 'q':
        break

    second_num = input('\nSecond number: ')

    if second_num == 'q':
        break

    try:
        answer = int(first_num) / int(second_num)

    except ZeroDivisionError:
        print("You can't divide by zero, bub!")

    else:
        print(answer)
