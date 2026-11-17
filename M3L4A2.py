
# DSCM4L4 Activity 2: Finding All Factors of a Number
# Run with Python or paste the complete program into Google Colab.
# Enter a whole number to check, or press Enter to skip the extra test.
# A factor divides a number exactly, leaving remainder 0.
# Factors can be found in pairs: divisor and number // divisor.


def get_input(message):
    """Accept a valid whole number or return None for empty or invalid input."""
    try:
        value = input(message).strip()
    except EOFError:
        return None

    if value == "":
        return None

    if not value.isdecimal() or len(value) > 13 or int(value) > 10 ** 12:
        print("Please type a whole number from 0 to 1000000000000, for example 36.")
        return None

    return int(value)


def find_all_factors(number):
    """Check every possible divisor from 1 to number. Time complexity: O(n)."""
    factor_list = []
    total_checks = 0

    for divisor in range(1, number + 1):
        total_checks += 1

        if number % divisor == 0:
            factor_list.append(divisor)

    return factor_list, total_checks


def find_factors_by_pairs(number):
    """Check divisors up to the square root and collect their matching factors."""
    lower_factors = []
    upper_factors = []
    total_checks = 0
    divisor = 1

    while divisor * divisor <= number:
        total_checks += 1

        if number % divisor == 0:
            lower_factors.append(divisor)

            partner = number // divisor
            if divisor != partner:
                upper_factors.append(partner)

        divisor += 1

    upper_factors.reverse()
    return lower_factors + upper_factors, total_checks


# Test the faster factor-finding method with sample numbers.
test_values = [36, 97, 100]

for number in test_values:
    result, pair_checks = find_factors_by_pairs(number)

    print(number, "has", len(result), "factors:", result)
    print("   checks: pairs", pair_checks, "  brute force", find_all_factors(number)[1])

print()

# Compare the number of checks for a larger value.
large_number = 1000000

print("n =", large_number, ": pairs", find_factors_by_pairs(large_number)[1],
      "checks, brute force", find_all_factors(large_number)[1], "checks")

print()

# Check a number entered by the user.
user_value = get_input("Type a whole number 1 or more (or press Enter to finish): ")

if user_value is None:
    print("No number checked.")
elif user_value == 0:
    print("0 has no list of factors: every number divides 0. Type 1 or more.")
else:
    result, total_checks = find_factors_by_pairs(user_value)
    print(user_value, "has", len(result), "factors:", result, "  checks:", total_checks)
