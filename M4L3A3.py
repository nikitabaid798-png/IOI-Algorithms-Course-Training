
# Activity 3: Separating Two Odd-Occurring Values
# Topic: XOR and the Rightmost Set Bit

input("XOR removes matching pairs and leaves two different values.  Press Enter ")

sample_values = [1, 4, 3, 3]
combined_xor = 0

for value in sample_values:
    combined_xor ^= value

print("  [1, 4, 3, 3]  XOR of all:",
      combined_xor, "  binary:", bin(combined_xor)[2:])
print("  split bit 1  ->  group A (bit 0 ON): 1   group B (bit 0 OFF): 4")

number = int(input("Enter a number (try 6 or 9): "))
guess = input("Is bit 0 of " + str(number) + " ON? (yes/no): ")

input("Use the last bit to identify the group.  Press Enter ")

if number & 1:
    print(" ", number, "  binary:", bin(number)[2:],
          "  bit 0 ON - group A  your guess:", guess)
else:
    print(" ", number, "  binary:", bin(number)[2:],
          "  bit 0 OFF - group B  your guess:", guess)
