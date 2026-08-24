# Program to print Fibonacci series using a function

# Function to generate Fibonacci series
def fibonacci_series(terms):
    first = 0
    second = 1

    # Check if the number of terms is valid
    if terms <= 0:
        print("Please enter a positive number.")
    else:
        print("Fibonacci series:")

        for count in range(terms):
            print(first, end=" ")

            # Calculate the next number
            next_number = first + second
            first = second
            second = next_number


# Ask the user for the number of terms
number_of_terms = int(input("Enter the number of terms: "))

# Call the function
fibonacci_series(number_of_terms)
