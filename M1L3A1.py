# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check whether the number is divisible by 2
if number % 2 == 0:
    # If the remainder is 0, the number is even
    print("The number is even.")
else:
    # If the remainder is not 0, the number is odd
    print("The number is odd.")
