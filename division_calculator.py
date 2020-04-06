### Chapter 10: Files and Exceptions

## Exceptions

# Handling the ZeroDivisionError Exception

""" This gracefully handles the ZeroDivisionError returned if program tries to divide by zero. """
try:
    print(5/0)

except ZeroDivisionError:
    print('Can\'t divide by zero.')


# 
