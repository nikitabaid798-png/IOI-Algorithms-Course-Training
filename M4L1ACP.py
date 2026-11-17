
# =================================
# SECRET CODE: BINARY SCANNER
# =================================
# Topics:
# Binary Numbers, AND, OR, NOT, XOR
# Left Shift, Right Shift, Parity and Counting Bits

secret_number = 13
key_number = 9


def show_binary(value, width=4):
    mask = (1 << width) - 1
    return format(value & mask, "0" + str(width) + "b")


print("================================")
print("MY SECRET CODE BIT SCANNER")
print("================================")

print("Secret Code:", secret_number, "Binary:", show_binary(secret_number))
print("Access Key:", key_number, "Binary:", show_binary(key_number))


# PART 1 - BITS AND BINARY
print("\nPART 1: Bits and Binary")
print("Binary numbers use only 0 and 1.")
print("Secret Code Binary:", show_binary(secret_number))
print("Access Key Binary:", show_binary(key_number))


# PART 2 - AND AND OR
and_value = secret_number & key_number
or_value = secret_number | key_number

print("\nPART 2: AND and OR")
print("AND Result:", and_value, "Binary:", show_binary(and_value))
print("OR Result:", or_value, "Binary:", show_binary(or_value))
print("AND keeps only positions where both bits are 1.")
print("OR keeps positions where at least one bit is 1.")


# PART 3 - NOT AND XOR
not_value = (~secret_number) & 0b1111
xor_value = secret_number ^ key_number

print("\nPART 3: NOT and XOR")
print("NOT Secret Code within 4 bits:", not_value, "Binary:", show_binary(not_value))
print("XOR Result:", xor_value, "Binary:", show_binary(xor_value))
print("XOR gives 1 when the compared bits are different.")


# PART 4 - SHIFTING BITS
left_value = secret_number << 1
right_value = secret_number >> 1

print("\nPART 4: Left Shift and Right Shift")
print("Left Shift Result:", left_value, "Binary:", show_binary(left_value, 5))
print("Right Shift Result:", right_value, "Binary:", show_binary(right_value))
print("Left shift moves bits left. Right shift moves bits right.")


# PART 5 - ODD OR EVEN USING XOR
parity_result = secret_number ^ 1

print("\nPART 5: Odd or Even with XOR")
print("Secret Code XOR 1:", parity_result)

if parity_result == secret_number - 1:
    print("Secret Code is Odd because XOR with 1 reduced it by 1.")
else:
    print("Secret Code is Even because XOR with 1 increased it by 1.")


# PART 6 - COUNTING BITS
ones_total = secret_number.bit_count()

print("\nPART 6: Counting Bits")
print("Number of 1 bits in Secret Code:", ones_total)


# FINAL SUMMARY
print("\n================================")
print("SECRET CODE SCAN SUMMARY")
print("================================")
print("Secret Code:", secret_number, "Binary:", show_binary(secret_number))
print("Access Key:", key_number, "Binary:", show_binary(key_number))
print("AND:", and_value)
print("OR:", or_value)
print("NOT within 4 bits:", not_value)
print("XOR:", xor_value)
print("Left Shift:", left_value)
print("Right Shift:", right_value)
print("1 Bits Count:", ones_total)
print("================================")
