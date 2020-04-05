### Chapter 8: Functions

## Positional Arguments
def describe_pet(animal_type, pet_name):
    """ Display information about a pet. """
    print(f"I have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet("hamster", "harry")


## Mutltiple Function Calls
describe_pet("dog", "willie")
describe_pet("cat", "cooter")


## Keyword Arguments
describe_pet(animal_type = "parrot", pet_name = "polly")
describe_pet(pet_name = "polly", animal_type = "parrot")


## Default Values
def describe_pet(pet_name, animal_type = "dog"):
    """ Default value for animal_type is "dog". """
    """ Display information about a pet. """
    print(f"I have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet("Lassie")


## Equivalent Function Calls
describe_pet("willie")
describe_pet(pet_name = "willie")

describe_pet("harry", "hamster")
describe_pet(pet_name = "harry", animal_type = "hamster")
describe_pet(animal_type = "hamster", pet_name = "harry")