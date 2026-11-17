
# DSCM4L4 After Class Project: Binary Number Converter
# Run this program in Python or Google Colab.
# Binary numbers contain only the digits 0 and 1.
# Each new digit is processed by multiplying the previous result by 2
# and then adding the current digit.


def convert_binary(binary_text):
    """Convert binary text into decimal and return the number of steps."""
    binary_text = binary_text.strip()

    if not binary_text:
        return None, 0

    decimal_result = 0
    operation_count = 0

    for bit in binary_text:

        # Reject the input if it contains an invalid binary digit.
        if bit != "0" and bit != "1":
            return None, 0

        # Update the decimal value using the current binary digit.
        decimal_result = (decimal_result * 2) + int(bit)

        operation_count += 1

    return decimal_result, operation_count


# Run the converter with different binary inputs.
binary_samples = ["1101", "010", "1000", "11111111", "1012", ""]

for binary_value in binary_samples:
    answer, steps_taken = convert_binary(binary_value)

    if answer is None:
        print(f"  '{binary_value}' is not a binary number (use only 0 and 1)")
    else:
        print(f"{binary_value:>12} -> {answer:<4} steps = {steps_taken}")

print()
print("Time: O(L) for L binary digits (one step per digit). Extra space: O(1).")
