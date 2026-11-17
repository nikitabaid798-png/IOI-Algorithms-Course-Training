
# DSCM4L5 Activity 2: Finding the Greatest Common Divisor
# Run this program using Python or Google Colab.
# The GCD (also called HCF) is the largest number that divides
# both given numbers without leaving a remainder.
# We will compare the brute-force approach with Euclid's algorithm.


def find_gcd_bruteforce(num1, num2):
    """Check possible divisors from largest to smallest and return (GCD, steps)."""
    check_count = 0

    for divisor in range(min(num1, num2), 0, -1):
        check_count += 1

        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor, check_count

    return max(num1, num2), check_count


def find_gcd_euclidean(num1, num2):
    """Use Euclid's method to calculate the GCD and return the number of steps."""
    operation_count = 0

    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
        operation_count += 1

    return num1, operation_count


def display_comparison(number1, number2):
    """Calculate the GCD using both methods and display their step counts."""
    result, euclid_count = find_gcd_euclidean(number1, number2)
    brute_result, brute_count = find_gcd_bruteforce(number1, number2)

    print(f"gcd({number1}, {number2}) = {result}   Euclid steps: {euclid_count}   brute-force steps: {brute_count}")


# Compare both approaches using sample number pairs.
test_pairs = [
    (16, 24),
    (24, 16),
    (12, 8),
    (1071, 462),
    (0, 5),
    (832040, 514229)
]

for a, b in test_pairs:
    display_comparison(a, b)

print()

# Ask the user to enter two numbers.
try:
    user_input = input("Type two whole numbers with a space between (or just press Enter to finish): ")
except EOFError:
    user_input = ""

values = user_input.split()

if not values:
    print("No numbers typed: demo only.")
else:
    try:
        first_number = int(values[0])
        second_number = int(values[1])

        if len(values) != 2 or first_number < 0 or second_number < 0 or first_number == second_number == 0:
            print("Please type exactly two whole numbers, 0 or more, not both 0.")
        else:
            display_comparison(first_number, second_number)

    except (ValueError, IndexError):
        print("Please type exactly two whole numbers, 0 or more, not both 0.")
