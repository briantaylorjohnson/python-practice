### Chapter 6

## Looping Through a Dictionary

# Loooping Through All Key-Value Pairs (Cont'd)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for name, language in favorite_languages.items(): # Variable name is assigned the key value; variable language is assigned the pair value
    print(f'{name.title()}\'s favorite language is {language.title()}.\n')

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys(): # Loops through all keys for favorite_languages dictionary
    print(name.title())

for name in favorite_languages: # Looping through the keys is the default behavior so this would have the same result
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f'\nHi {name.title()}!')

    if name in friends:
        language = favorite_languages[name].title() # The name key can be used to look up the value for language in the dictionary
        print(f'\t{name.title()}, I see you love {language}.')

if 'erin' not in favorite_languages.keys(): # keys() method used to see if a person (key) took the poll
    print('\nErin, please take our poll.\n')

# Looping Through a Dictionary's Keys in a Particular Order
# Default is to loop through the keys in the order they were inserted

for name in sorted(favorite_languages.keys()): # Loops through the dictionary's keys in a sorted order
    print(f'{name.title()}, thank you for taking the poll.\n')

# Looping Through All Values in a Dictionary
print('The following languages have been meantioned:')
for language in favorite_languages.values(): # Loops through all the values -- including duplicates
    print(language.title())
print('\n')

for language in set(favorite_languages.values()): # Loops through only unique values using the set() method
    print(language.title())
print('\n')

languages = {'python', 'ruby', 'python', 'c'} # A set can be created using just braces and values -- not square brackets as that would create a list that includes the duplicates
print(languages)

