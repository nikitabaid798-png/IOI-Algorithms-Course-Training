
# Activity 1: Clearing the Rightmost Set Bit
# Topic: n & (n-1) and Power of 2 Detection

input("AND with n-1 removes the rightmost 1 bit.  Press Enter ")

first_number = 12
second_number = 8

print("  12 & 11 =", first_number & 11,
      "  binary:", bin(first_number & 11)[2:])
print("  8 & 7 =", second_number & 7)

value = int(input("Enter a number (try 4 or 6): "))
prediction = input("Is " + str(value) + " a power of 2? (yes/no): ")

input("A power of 2 has exactly one set bit.  Press Enter ")

binary_value = bin(value)[2:]

if value > 0 and (value & (value - 1)) == 0:
    print(" ", value, "  binary:", binary_value,
          "  power of 2: yes  your guess:", prediction)
else:
    print(" ", value, "  binary:", binary_value,
          "  power of 2: no   your guess:", prediction)
