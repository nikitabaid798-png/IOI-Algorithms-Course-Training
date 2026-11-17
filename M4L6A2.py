
# Activity 2: Checking Individual Bits

input("To inspect a bit, shift it to the right and use AND with 1. Press Enter ")

print("  Number 12:", bin(12)[2:])
print("  Bit 2:", (12 >> 2) & 1, " Bit 1:", (12 >> 1) & 1)

print("  Number 7:", bin(7)[2:])
print("  Bit 2:", (7 >> 2) & 1, " Bit 1:", (7 >> 1) & 1)

value = int(input("Enter a number (try 9 or 6): "))

print("  Binary form:", bin(value)[2:])

prediction = input("What value is stored at bit position 2? (0 or 1): ")

input("Right shifting by 2 and applying AND with 1 extracts that bit. Press Enter ")

selected_bit = (value >> 2) & 1

print("  Number:", value)
print("  Value at bit 2:", selected_bit)
print("  Your prediction:", prediction)
