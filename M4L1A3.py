
# Activity 3: Checking Odd/Even and Counting Binary Ones

input("Parity — last bit = 0 even,  last bit = 1 odd.  Press Enter ")

test_values = [2, 3, 4, 5, 8, 9]

for value in test_values:
    last_bit = value & 1

    if last_bit == 1:
        print("  ", value, "->  odd")
    else:
        print("  ", value, "->  even")

number = int(input("Enter a number (try 13 or 7): "))

input("Count the 1s — watch bits drop off.  Press Enter ")

remaining = number

while remaining > 0:
    current_binary = bin(remaining)[2:]
    last_digit = remaining & 1

    print("  binary:", current_binary, "  last bit:", last_digit)

    remaining = remaining >> 1

ones_count = bin(number).count("1")
print("  total 1s in", number, "=", ones_count)
