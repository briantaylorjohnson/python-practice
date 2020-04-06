### Chapter 9: Classes 

## Creating and Using a Class

# Creating the Dog Class

class Dog:

    """ A simple attempt to model a dog. """
    def __init__(self, name, age):

        """ Initialize name age attributes. """
        self.name = name
        self.age = age


    def sit(self):

        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting.")


    def roll_over(self):

        """ Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over!")


# Making an Instance from a Class

my_dog = Dog("Willie", 6) # Instantiates an object of the class Dog

print(f"My dog\'s name is {my_dog.name}.") # Accesses the dog's name with my_dog.name
print(f"My dog is {my_dog.age} years old.") # Access the dog's age with my_dog.age

my_dog.sit() # Called the sit() method
my_dog.roll_over() # Called the roll_over() method

print("")

your_dog = Dog("Lucy", 3) # Creates a second instance/object of the class Dog

print(f"Your dog\'s name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()

