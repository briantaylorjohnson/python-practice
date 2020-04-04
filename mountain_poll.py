### Chapter 7

## Using while loops with Lists and Dictionaries

# Filling a dictionary with user input

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:

    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("What mountain would you like to climb one day? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another person respond? (yes/no) ")

    if repeat == "no": # Exits the loop by setting flag to False if user's response to prompt is 'no'

        polling_active = False

# Polling is complete. Show the results.

print("\n<-------- Poll Results -------->")

for name, response in responses.items(): # Iterates through dictionary to output key-value (name-response) pairs

    print(f"{name} would like to climb {response}.")


print("<------------------------------>")

