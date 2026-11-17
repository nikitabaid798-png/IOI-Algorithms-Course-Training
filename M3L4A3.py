
# DSCM4L4 Activity 3: Converting Roman Numerals into Integers
# Run using Python or paste the complete code into Google Colab.
# Enter a Roman numeral to convert it, or press Enter to skip.
# If a smaller Roman numeral appears before a larger one, subtract its value.
# Otherwise, add the value to the total.
# Example: IV = -1 + 5 = 4 and XC = -10 + 100 = 90.

ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def convert_roman(numeral):
    """Convert a Roman numeral into an integer and count the processed letters."""
    numeral = numeral.strip().upper()

    if numeral == "":
        return None, 0

    # Make sure every character is a valid Roman numeral symbol.
    for symbol in numeral:
        if symbol not in ROMAN_VALUES:
            return None, 0

    result = 0
    letter_count = 0

    for position in range(len(numeral)):
        current_value = ROMAN_VALUES[numeral[position]]

        # Subtract the current value if the next symbol is larger.
        if position + 1 < len(numeral) and current_value < ROMAN_VALUES[numeral[position + 1]]:
            result -= current_value
        else:
            result += current_value

        letter_count += 1

    return result, letter_count


def display_result(roman_text):
    """Display the converted number or an error message."""
    converted_value, steps = convert_roman(roman_text)

    if converted_value is None:
        print(f"  '{roman_text}' is not a Roman numeral (use only I V X L C D M)")
    else:
        print(f"{roman_text:>10} = {converted_value:<5} steps = {steps}")


# Try the converter with different Roman numerals.
examples = ["III", "IX", "LVIII", "LXXVII", "MCMXCIV", "xiv"]

for item in examples:
    display_result(item)

print()

# Get an additional Roman numeral from the user.
try:
    user_numeral = input("Type a Roman numeral (or press Enter to finish): ").strip()
except EOFError:
    user_numeral = ""

if user_numeral == "":
    print("No numeral checked.")
else:
    display_result(user_numeral)
