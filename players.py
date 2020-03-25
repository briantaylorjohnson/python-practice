# Chapter 4

# Slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli'] # Initial list of players

print(players[0:3]) # Specifies where to start and stop the slice of the list (exclusive of the ending index)

print(players[1:4]) # Specifies where to start and stop the slice of the list (exclusive of the ending index)

print(players[:4]) # Leaving off the start index will begin the slice from index of 0

print(players[2:]) # Leaving off the stop index will end the slice with the last element

print(players[-2:]) # A negative start index will return the last x elements in the list


print("\n") # New line

# Looping through a slice

print("Here are the first three players on my team:")

for player in players[:3]:
	print(player.title())






