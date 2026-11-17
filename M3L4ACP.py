
# DSCM4L4 After Class Project: Converting Binary to Decimal
# Run using Python or paste the complete code into Google Colab.
# Binary numbers contain only 0 and 1.
# Read each digit from left to right, doubling the current value
# and adding the next digit.

def binary_to_decimal(bits):
    """Return (decimal value, steps), or (None, 0) for invalid input."""
    bits = bits.strip()

    if bits == "":
        return None, 0

    value = 0
    steps = 0

    for digit in bits:
        # TODO 1: Check whether the current digit is valid.
        if digit not in "01":
            return None, 0

        # TODO 2: Double the current value and add the binary digit.
        value = value * 2 + int(digit)

        steps = steps + 1

    return value, steps


# A: Test the function with six different inputs.
for bits in ["1101", "010", "1000", "11111111", "1012", ""]:
    value, steps = binary_to_decimal(bits)

    if value is None:
        print(f"  '{bits}' is not a binary number (use only 0 and 1)")
    else:
        print(f"{bits:>12} -> {value:<4} steps = {steps}")

print()
print("Time: O(L) for L binary digits (one step per digit). Extra space: O(1).")
