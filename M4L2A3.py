
# Activity 3: Creating Masks and Checking Individual Bits

input("Create a mask with one set bit.  Press Enter ")

for position in range(4):
    bit_mask = 2 ** position
    print("  bit", position, "  mask:", bit_mask,
          "  binary:", bin(bit_mask)[2:])

number = int(input("Enter a number (try 42 or 13): "))
user_answer = input("Is bit 2 of " + str(number) + " ON? (yes/no): ")

input("Use AND to check whether a particular bit is ON.  Press Enter ")

checked_bit = (number >> 2) & 1
binary_number = bin(number)[2:]

if checked_bit == 1:
    print(" ", number, "  binary:", binary_number,
          "  bit 2 is ON  your guess:", user_answer)
else:
    print(" ", number, "  binary:", binary_number,
          "  bit 2 is OFF  your guess:", user_answer)
