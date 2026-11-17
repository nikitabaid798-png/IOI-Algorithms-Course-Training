
# =================================
# BITWISE OPERATIONS CHALLENGE
# =================================
# Topics:
# Swapping Without an Extra Variable
# XOR Swap
# Left Shift
# XOR Sign Detection
# Division Using Repeated Subtraction

print("================================")
print("BITWISE SWAP CHALLENGE")
print("================================")


# ---------------------------------
# PART 1 - SWAPPING USING ADDITION
# ---------------------------------

first_value = 56
second_value = 12

print("\nPART 1: Swap Without a Third Variable")
print("Before Swap:")
print("a =", first_value)
print("b =", second_value)

first_value = first_value + second_value
second_value = first_value - second_value
first_value = first_value - second_value

print("After Swap:")
print("a =", first_value)
print("b =", second_value)


# ---------------------------------
# PART 2 - SWAPPING USING XOR
# ---------------------------------

left = 45
right = 18

print("\nPART 2: XOR Swap")
print("Before XOR Swap:")
print("x =", left)
print("y =", right)

left ^= right
right ^= left
left ^= right

print("After XOR Swap:")
print("x =", left)
print("y =", right)


# ---------------------------------
# PART 3 - MULTIPLYING WITH LEFT SHIFT
# ---------------------------------

base_number = 3

print("\nPART 3: Left Shift Doubles the Number")
print("Original Number:", base_number)

for shift in range(1, 5):
    shifted_result = base_number << shift
    print(base_number, "<<", shift, "=", shifted_result)

print("Each left shift multiplies the number by 2.")


# ---------------------------------
# PART 4 - DETECTING DIFFERENT SIGNS
# ---------------------------------

value_one = -10
value_two = 5

print("\nPART 4: XOR for Sign Detection")
print("num1 =", value_one)
print("num2 =", value_two)

if (value_one < 0) ^ (value_two < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")


# ---------------------------------
# PART 5 - DIVISION WITHOUT /
# ---------------------------------

total = 25
divider = 4

answer = 0
remaining = total

while remaining >= divider:
    remaining -= divider
    answer += 1

print("\nPART 5: Divide Without /")
print("Dividend:", total)
print("Divisor:", divider)
print("Quotient:", answer)
print("Remainder:", remaining)


# ---------------------------------
# FINAL SUMMARY
# ---------------------------------

print("\n================================")
print("BITWISE SWAP CHALLENGE SUMMARY")
print("================================")
print("Swap without third variable uses addition and subtraction.")
print("XOR swap uses the ^ operator to swap values.")
print("Left shift doubles a number.")
print("XOR can help detect different signs.")
print("Division can be done using repeated subtraction.")
print("================================")
