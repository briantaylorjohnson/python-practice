### Chapter 10: Files and Exceptions

## Storing Data

# Saving and Reading User-Generated Data (Cont'd)

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username1.json'

try:

    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input('What is your name? ')

    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'We\'ll remember you when you come back, {username}.')

else:
    print(f'Welcome back, {username}...')