
# Activity 2: Find the Number That Appears Once
# XOR removes numbers that occur in pairs.

input("Combine the numbers using XOR.  Press Enter ")

sample = [2, 3, 4, 3, 2]
sample_result = 0

for value in sample:
    sample_result ^= value

print("  list:", sample)
print("  odd-occurring:", sample_result)

number = int(input("Enter a number (try 7 or 11): "))

values = [3, number, 5, 3, 5]
guess = input("Which number in " + str(values) + " appears once? ")

unique_value = 0

for item in values:
    unique_value = unique_value ^ item

input("Matching pairs cancel out, leaving one number.  Press Enter ")

print("  list:", values,
      "  odd-occurring:", unique_value,
      "  your guess:", guess)
