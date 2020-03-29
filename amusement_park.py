### Chapter 5

# IF Statements (Cont'd)

## IF-ELIF-ELSE Chain
age = 17

if age < 4:
    print("Your admission cost is $0.\n")

elif age < 18:
    print("Your admission cost is $25.\n")

else:
    print("Your admission cost is $40.\n")

# Using Multiple ELIF Blocks
age = 66

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.\n")
