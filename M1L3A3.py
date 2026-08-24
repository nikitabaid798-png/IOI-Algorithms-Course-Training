# Ask the user to enter a number for the first time
number1 = int(input("Enter a number: "))

# Ask the user to enter the number again
number2 = int(input("Enter the number again: "))

# Check if both numbers are the same
if number1 == number2:
    print("The numbers match.")
else:
    print("The numbers do not match.")
