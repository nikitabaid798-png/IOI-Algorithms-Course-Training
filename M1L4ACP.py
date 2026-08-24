# Program to check whether a number is an Armstrong number

# Take a number from the user
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Count the number of digits
digits = len(str(number))

# Start the sum from 0
total = 0

# Find each digit and calculate its power
while number > 0:
    digit = number % 10
    total = total + digit ** digits
    number = number // 10

# Check whether the calculated sum matches the original number
if total == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
