# Program to find whether a number is prime or not

# Get a number from the user
number = int(input("Enter a number: "))

# A prime number must be greater than 1
if number > 1:

    # Check for factors from 2 up to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):

        # Check if the number is exactly divisible
        if number % divisor == 0:
            print(f"{number} is not a prime number.")
            break

    else:
        # No factor was found, so the number is prime
        print(f"{number} is a prime number.")

else:
    # Numbers 1 and below are not prime
    print(f"{number} is not a prime number.")
