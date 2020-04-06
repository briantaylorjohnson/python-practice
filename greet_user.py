### Chapter 10: Files and Exceptions

## Storing Data

# Saving and Reading User-Generated Data (Cont'd)

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f'Welcome back, {username}...')