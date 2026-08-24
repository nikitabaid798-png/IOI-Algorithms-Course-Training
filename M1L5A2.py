# Program to find the factorial using recursion

def calculate_factorial(value):
    # Base condition for recursion
    if value == 1:
        return value
    else:
        # Call the function again with the previous number
        return value * calculate_factorial(value - 1)


# Get a number from the user
number = int(input("Enter a number: "))

# Check whether the entered number is negative
if number < 0:
    print("Factorial is not possible for negative numbers.")

elif number == 0:
    print("The factorial of 0 is 1.")

else:
    print("The factorial of", number, "is", calculate_factorial(number))
