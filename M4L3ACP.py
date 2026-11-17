
# =================================
# BINARY PUZZLE: CLUE INVESTIGATOR
# =================================
# Topics:
# XOR Identity and Equality
# XOR Cancellation
# One Odd-Occurring Number
# Two Odd-Occurring Numbers
# Splitting Using the Rightmost Set Bit

print("================================")
print("BINARY CLUE INVESTIGATOR")
print("================================")


# ---------------------------------
# PART 1 - XOR IDENTITY AND EQUALITY
# ---------------------------------

first_num = 7
second_num = 7

print("\nPART 1: XOR Identity and Equality")
print("a =", first_num)
print("b =", second_num)
print("a ^ a =", first_num ^ first_num)
print("a ^ 0 =", first_num ^ 0)

if (first_num ^ second_num) == 0:
    print("Both numbers are equal")
else:
    print("Both numbers are different")


# ---------------------------------
# PART 2 - XOR CANCELLATION
# ---------------------------------

clue_list = [3, 5, 3, 5, 9]

combined_result = 0

for value in clue_list:
    combined_result ^= value

print("\nPART 2: XOR Cancellation")
print("Clues:", clue_list)
print("Final XOR Result:", combined_result)
print("Repeated clues cancel out, so the remaining clue is:", combined_result)


# ---------------------------------
# PART 3 - ONE ODD-OCCURRING NUMBER
# ---------------------------------

data = [4, 7, 4, 2, 7, 2, 9]

single_value = 0

for item in data:
    single_value ^= item

print("\nPART 3: One Odd-Occurring Number")
print("Numbers:", data)
print("Odd-occurring number:", single_value)


# ---------------------------------
# PART 4 - TWO ODD-OCCURRING NUMBERS
# ---------------------------------

mixed_values = [3, 9, 3, 5, 5, 7]

total_xor = 0

for item in mixed_values:
    total_xor = total_xor ^ item

print("\nPART 4: XOR of Two Odd-Occurring Numbers")
print("Numbers:", mixed_values)
print("XOR of two odd-occurring numbers:", total_xor)


# ---------------------------------
# PART 5 - SPLITTING USING THE RIGHTMOST SET BIT
# ---------------------------------

lowest_bit = total_xor & -total_xor

group_one = 0
group_two = 0

for item in mixed_values:
    if item & lowest_bit:
        group_one ^= item
    else:
        group_two ^= item

print("\nPART 5: Splitting by the Rightmost Set Bit")
print("Rightmost set bit:", lowest_bit)
print("First odd-occurring number:", group_one)
print("Second odd-occurring number:", group_two)


# ---------------------------------
# FINAL SUMMARY
# ---------------------------------

print("\n================================")
print("BINARY CLUE INVESTIGATION SUMMARY")
print("================================")
print("XOR Identity: a ^ a = 0")
print("XOR with zero: a ^ 0 = a")
print("XOR Cancellation removes repeated pairs")
print("One odd-occurring number found:", single_value)
print("Two odd-occurring numbers found:", group_one, "and", group_two)
print("================================")
