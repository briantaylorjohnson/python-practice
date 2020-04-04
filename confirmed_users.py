### Chapter 7

## Using a while loop with Lists and Dictionaries

# Moving items from one list to another

users = ["Tina", "Tom", "Travis", "Terri"]

confirmed_users = []

# The while loop moves each unconfirmed users in the users list to the confirmed_users list
while users:
    current_user = users.pop() # Retrieves the last item in the users list and assigns it to the current_user variable

    print(f"Verifying user: {current_user.title()}")
    
    confirmed_users.append(current_user) # Add the current_user to the confirmed_users list

print("\nThe following users have been confirmed: ")

# The for loop prints all confirmed users in the confirmed_users list
for confirmed_user in confirmed_users:

    print(confirmed_user.title())