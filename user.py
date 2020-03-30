### Chapter 6

## Looping Through a Dictionary

# Loooping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for k, v in user_0.items(): # Abbreviations can be used for key and value
    print(f'\nKey: {key}')
    print(f'Value: {value}')