
# Activity 3: Finding Different Bits with XOR

input("XOR gives 1 wherever two numbers have different bits. Press Enter ")

first_result = 5 ^ 3
second_result = 9 ^ 5

print("  5 XOR 3 =", first_result)
print("  Binary:", bin(first_result)[2:])
print("  Different bit count:", bin(first_result).count("1"))

print("  9 XOR 5 =", second_result)
print("  Binary:", bin(second_result)[2:])
print("  Different bit count:", bin(second_result).count("1"))

number = int(input("Enter a number (try 4 or 6): "))

guess = input("How many bit positions differ between " + str(number) + " and 7? ")

input("Count the number of 1s in the XOR result to find the answer. Press Enter ")

xor_value = number ^ 7
different_count = bin(xor_value).count("1")

print("  XOR result:", number, "^ 7 =", xor_value)
print("  Binary result:", bin(xor_value)[2:])
print("  Number of different bits:", different_count)
print("  Your prediction:", guess)
