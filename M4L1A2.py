
# Activity 2: Exploring NOT, XOR and Bit Shifts

value = int(input("Enter a number (try 5 or 12): "))
student_guess = input(
    "Left shift doubles it. Guess: " + str(value) + " << 1 = ? "
)

input("NOT — flips every bit.  Press Enter ")
binary_form = bin(12)[2:]
not_answer = (~12) & 255

print("  12 =", binary_form)
print("  NOT 12 =", not_answer)

input("XOR — different bits give 1.  Press Enter ")
xor_answer = 12 ^ 10
print("  12 ^ 10 =", xor_answer)

input("Left shift — multiplies by 2.  Press Enter ")
left_result = value << 1
print("  ", value, "<< 1 =", left_result, "  your guess:", student_guess)

input("Right shift — divides by 2.  Press Enter ")
right_result = value >> 1
print("  ", value, ">> 1 =", right_result)
