# Chapter 3
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] # List of elements in brackets separated by commas
print(bicycles) # Printing a list includes the brackets, commas, and apostrophes/quotation marks

print(bicycles[0]) # Print element in bicycles list at index 0
print(bicycles[0].title()) # Print element in bicycles list at index 0 with title case
print(bicycles[-1].title()) # Using an index of -1 always returns the last element in the list

message = f"My first bike was a {bicycles[0].title()}." # Use f-strings with list elements
print(message) 