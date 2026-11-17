
# DSCM4L4 Activity 1: Checking Armstrong Numbers
# Run using: python3 armstrong.py or paste the code into Google Colab.
# Enter a whole number to check it, or press Enter to skip the check.
# An Armstrong number is equal to the sum of its digits raised to
# the power of the total number of digits.
# Example: 153 = 1**3 + 5**3 + 3**3 = 153.


def get_number(message):
    """Read a valid whole number. Return None if input is empty or invalid."""
    try:
        value = input(message).strip()
    except EOFError:
        return None

    if value == "":
        return None

    if not value.isdecimal() or len(value) > 1000:
        print("Please type a whole number like 153 (digits only, at most 1000 of them).")
        return None

    return int(value)


def check_armstrong(number):
    """Check whether a number is Armstrong and count the digit-processing steps."""
    digit_count = len(str(number))
    digit_sum = 0
    step_count = 0
    current = number

    while current > 0:
        last_digit = current % 10
        digit_sum += last_digit ** digit_count
        current //= 10
        step_count += 1

    return digit_sum == number, step_count


# Check some sample numbers.
sample_numbers = [0, 1, 9, 10, 153, 154, 370, 371, 407, 9474]

for number in sample_numbers:
    result, steps = check_armstrong(number)

    if result:
        print(f"{number:>5} is an Armstrong number      digit steps = {steps}")
    else:
        print(f"{number:>5} is not an Armstrong number  digit steps = {steps}")

print()

# Allow the user to enter another number.
user_number = get_number("Type a whole number to check (or press Enter to finish): ")

if user_number is None:
    print("No number checked.")
else:
    result, steps = check_armstrong(user_number)
    print(user_number, "is an Armstrong number:", result, "  digit steps =", steps)
