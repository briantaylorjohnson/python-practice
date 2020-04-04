### Chapter 7

## More while loops: Uing continue in a loop

# Here we use the continue to print only the odd numbers

current_num = 0

while current_num < 10:

    current_num += 1

    if current_num % 2 == 0: # Continue stops the loop from executing the remaining code in the loop and restarts it
        continue

    print(current_num)


print("\n")

## Avoiding infinite loops

# This loops only until x > 5
x = 1

while x <= 5:

    print(x)
    x += 1

# This infinitely loops
# x = 1
#
# while x <= 5:
#
#   print(x) # Variable x will always be 1 and thusly will always be <= 5