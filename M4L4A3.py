
# Activity 3: Calculating Powers with Binary Exponentiation

input("Binary exponentiation works by reading exponent bits.  Press Enter ")

print("  2^8 = 256   exponent 8 = binary", format(8, "b"))
print("  2^5 = 32    exponent 5 = binary", format(5, "b"))

power = int(input("Enter exponent (try 3 or 6): "))

print("  exponent", power, "= binary", bin(power)[2:])

answer_guess = input("What is 2^" + str(power) + "? ")

input("The exponent's binary representation helps calculate the power.  Press Enter ")

final_answer = 2 ** power

print("  2^", power, "=", final_answer, "  your guess:", answer_guess)
