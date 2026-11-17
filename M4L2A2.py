
# Activity 2: Locating the First Set Bit
# The first set bit is the rightmost 1 in binary.

input("Let's find the rightmost 1 bit.  Press Enter ")

print("   5  ->  binary:", format(5, "b"), "  first 1 at position 0")
print("   8  ->  binary:", format(8, "b"), "  first 1 at position 3")

number = int(input("Enter a number (try 8 or 14): "))

input("Keep shifting right until the first 1 is found.  Press Enter ")

current = number
bit_position = 0

while current > 0:
    last_digit = current & 1
    print("  binary:", bin(current)[2:], "  last bit:", last_digit)

    if last_digit == 1:
        break

    bit_position += 1
    current = current >> 1

print("  first set bit in", number, "is at position", bit_position)
