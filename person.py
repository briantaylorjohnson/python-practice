### Chapter 8: Functions

## Returning a Dictionary
def build_person(first_name, last_name):
    """ Returning a dictionary of information about a person. """

    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person("jimi", "hendrix")
print(musician)


## Returning a Dictionary (Cont'd) with Optional Arguments
def build_person(first_name, last_name, age = None):
    """ Returning a dictionary of information about a person. """

    person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age

    return person

musician = build_person("darius", "rucker", 51)
print(musician)

musician = build_person("lee", "greenwood")
print(musician)