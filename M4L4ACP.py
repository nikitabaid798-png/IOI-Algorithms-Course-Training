
# =================================
# BINARY POWER DETECTOR
# =================================
# Topics:
# n & (n-1) Trick
# Power of 2, Power of 4 and Power of 8
# Binary Exponentiation

print("================================")
print("POWER OF TWO SCANNER")
print("================================")


# ---------------------------------
# PART 1 - THE n & (n-1) TRICK
# ---------------------------------

value = 16
reduced_value = value & (value - 1)

print("\nPART 1: The n & (n-1) Trick")
print("n       =", value, "->", bin(value))
print("n - 1   =", value - 1, "->", bin(value - 1))
print("n&(n-1) =", reduced_value, "->", bin(reduced_value))

print("\nThis trick removes the rightmost set bit.")


# ---------------------------------
# PART 2 - CHECKING POWER OF 2
# ---------------------------------

def check_power_two(number):
    return number > 0 and (number & (number - 1)) == 0


print("\nPART 2: Power of 2 Check")

test_numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

for item in test_numbers:
    result = check_power_two(item)
    print(item, "->", bin(item), "->", result)


# ---------------------------------
# PART 3 - CHECKING POWER OF 4
# ---------------------------------

def check_power_four(number):
    if not check_power_two(number):
        return False

    bit_index = 0

    while number > 1:
        number >>= 1
        bit_index += 1

    return bit_index % 2 == 0


print("\nPART 3: Power of 4 Check")

for item in test_numbers:
    print(item, "->", check_power_four(item))


# ---------------------------------
# PART 4 - CHECKING POWER OF 8
# ---------------------------------

def check_power_eight(number):
    if not check_power_two(number):
        return False

    bit_index = 0

    while number > 1:
        number >>= 1
        bit_index += 1

    return bit_index % 3 == 0


print("\nPART 4: Power of 8 Check")

for item in test_numbers:
    print(item, "->", check_power_eight(item))


# ---------------------------------
# PART 5 - BINARY EXPONENTIATION
# ---------------------------------

def calculate_power(base, exponent):
    result = 1

    while exponent > 0:
        if exponent & 1:
            result *= base

        base *= base
        exponent >>= 1

    return result


print("\nPART 5: Binary Exponentiation")
print("2^5 =", calculate_power(2, 5))
print("3^4 =", calculate_power(3, 4))
print("5^3 =", calculate_power(5, 3))


# ---------------------------------
# FINAL SUMMARY
# ---------------------------------

print("\n================================")
print("POWER SCANNER SUMMARY")
print("================================")
print("Power of 2: only one bit is set.")
print("Power of 4: set-bit position is even.")
print("Power of 8: set-bit position is divisible by 3.")
print("Binary exponentiation calculates powers quickly.")
print("================================")
