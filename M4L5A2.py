
# Activity 2: Performing Multiplication and Division with Shifts
# Left shift multiplies by powers of 2.
# Right shift divides by powers of 2.

input("Left shift doubles; right shift halves.  Press Enter ")

print("  3 << 1 =", 3 << 1, "   12 >> 1 =", 12 >> 1)
print("  3 << 2 =", 3 << 2, "   12 >> 2 =", 12 >> 2)

value = int(input("Enter a number (try 5 or 8): "))
guess = input("What is " + str(value) + " << 2? ")

input("Shifting left by two positions multiplies by four.  Press Enter ")

result = value << 2

print(" ", value, "<< 2 =", result, "  your guess:", guess)
