### Chapter 6

## Nesting

# A List in a Dictionary

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items(): # Loops through all the key-value (name-language list) pairs
    print(f'\n{name.title()}\'s favorite languages are:')

    for language in languages: # Loops through each key's (name) language list to return the favorite languages
        print(f'\t{language.title()}')
