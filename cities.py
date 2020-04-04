### Chapter 7

## Using break to exit a loop

# Break will exit the while loop immediately without running any more code in the loop
# A break can be used in any of Python's loops

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit': # Exits the loop when user enters 'quit' by using break (which essentially makes the while loop not true or false)
        break

    else:
        print(f"\nI'd love to go to {city.title()}.")