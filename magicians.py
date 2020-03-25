# Chapter 4
magicians = ['alice', 'david', 'carolina'] # Initial list of magicians

for magician in magicians: # For loop where magician is each element in magicians list and each element is printed
	print(magician)

print("\n") # New line

for magician in magicians: # For loop where magician is each element in magicians list and a message is printed with f-strings 
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")

# Indentation is used to specify all the steps in the for loop
# Remove the indentation for code to be executed after the for loop completes
print("That was a great show! Thank you everyone for attending.")