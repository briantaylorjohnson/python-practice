### Chapter 7

## Using the while loop to let the user choose when to quit

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit": # While loop will run as long as message is not equal to 'quit'

    message = input(prompt)

    if message != "quit": # Only outputs the message if message is not equal to 'quit'
        
        print(message) # Outputs the message

    else: 
        print("\n") # Creates a new line before quitting the program


## Using a flag to exit a loop

active = True

while active: # While loop only runs when active equals True
    message = input(prompt)

    if message == "quit": # Sets active to False if 'quit' is entered by the user and exits the loop to end the program
        active = False

    else:
        print(message) # Outputs the message if anything other than 'quit' is entered by the user







