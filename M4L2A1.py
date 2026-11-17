
# Activity 1: Switching Bits ON and OFF
# Topic: Set Bits, Zero Bits and Power of 2

input("Turn a bit ON using OR.  Press Enter ")
value = 5
updated_value = value | 2

print("  Original number:", value, "Binary:", bin(value)[2:])
print("  After OR:", updated_value, "Binary:", bin(updated_value)[2:])

input("Turn a bit OFF using AND.  Press Enter ")
value = 7
cleared_value = value & 5

print("  Original number:", value, "Binary:", bin(value)[2:])
print("  After AND:", cleared_value, "Binary:", bin(cleared_value)[2:])

number = int(input("Enter a number (try 4 or 6): "))
answer = input("Is it a power of 2? (yes/no): ")

input("A power of 2 has only one set bit.  Press Enter ")

binary_number = bin(number)[2:]

if number > 0 and (number & (number - 1)) == 0:
    print(" ", number, "  binary:", binary_number,
          "  power of 2  your guess:", answer)
else:
    print(" ", number, "  binary:", binary_number,
          "  not power of 2  your guess:", answer)
