# Python calculator using functions

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    return a / b


# Take two numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Display the available operations
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Ask the user to choose an operation
choice = int(input("Enter your choice (1-4): "))

# Perform the selected operation
if choice == 1:
    print("Result:", add_numbers(first_number, second_number))

elif choice == 2:
    print("Result:", subtract_numbers(first_number, second_number))

elif choice == 3:
    print("Result:", multiply_numbers(first_number, second_number))

elif choice == 4:
    if second_number != 0:
        print("Result:", divide_numbers(first_number, second_number))
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")
