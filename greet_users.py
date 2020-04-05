### Chapter 8: Functions

## Passing a List

def greet_users(names):
    """ Print a simple greeting to each users in a the list. """

    for name in names:
        msg = f"Hello, {name.title()}! Have a nice day."
        print(msg)

usernames = ["hannah", "ty", "bobby", "lance", "cindy"]

greet_users(usernames)