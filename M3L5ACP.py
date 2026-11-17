# Ask the user to input numbers 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find out which number is bigger.
if num1 > num2:
    greater = num1
else:
    greater = num2

# Keep looping until we find a number that can be divided by both num1 and num2
while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break # Stop the loop once we find it
    greater += 1 # Check the next number

# Print the final answer
print("The LCM of", num1, "and", num2, "is:", lcm)
