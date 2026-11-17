
# Activity 3: Checking Number Signs with XOR

input("XOR sign detection - a negative result indicates different signs.  Press Enter ")

print("  4 ^ 2 =", 4 ^ 2, "  same signs  positive")
print("  4 ^ -2 =", 4 ^ -2, "  different signs  negative")

number = int(input("Enter a number (try 5 or -3): "))
prediction = input(
    "Will " + str(number) + " ^ -8 be positive or negative? "
)

input("XOR produces a negative result when the signs differ.  Press Enter ")

xor_result = number ^ -8

print(" ", number, "^ -8 =", xor_result, "  your guess:", prediction)
