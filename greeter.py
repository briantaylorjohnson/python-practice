### Chapter 7 

## User Input

# Writing Clear Prompts

name = input("Please enter your name: ") # Space at end of prompt is clearer to user

print(f"\nHello, {name}!")


# Building a prompt over multiple lines can make the code cleaner
prompt = "If you tell us who you are, we can personalize the message you see."

prompt += "\nWhat is your name? "

name = input(prompt)

print(f"\nHello, {name}!")


#Using int() to accept numerical input

age = input("How old are you? ")

# age += 1      <-- This will cause the program to throw an error because input for variable age is interpretted as a string

age = int(age) + 1 # Converts variable age to an integer then adds 1, and then sets the value to the age variable as an int

print(f"In one year you will be {age}") # Notice the output is a string because the int() function wasn't used