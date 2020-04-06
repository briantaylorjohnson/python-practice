### Chapter 10: Files and Exceptions

## Storing Data

# Using json.dump() and json.load() (Cont'd)

import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)