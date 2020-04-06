### Chapter 10: Files and Exceptions

## Storing Data

# Using json.dump() and json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

print(numbers)