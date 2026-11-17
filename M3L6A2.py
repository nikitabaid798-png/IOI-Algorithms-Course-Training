
# DSCM4L6 Activity 1: Prime Number Checker
# Run this program in Python or Google Colab.
# A number is prime if it has exactly two factors: 1 and itself.
# Instead of checking every possible divisor, we stop at the square root.


def test_prime(value):
    """Check if a number is prime and return the result with its check count."""
    divisions = 0

    if value < 2:
        return False, divisions

    factor = 2

    while factor ** 2 <= value:
        divisions += 1

        if value % factor == 0:
            return False, divisions

        factor += 1

    return True, divisions


def get_brute_count(value):
    """Count the division checks made by the basic trial division approach."""
    divisions = 0

    for factor in range(2, value):
        divisions += 1

        if value % factor == 0:
            break

    return divisions


# Read and validate the number entered by the user.
entered_value = input("Type a whole number to test: ").strip()

if entered_value.isdecimal() and len(entered_value) <= 13 and int(entered_value) <= 10 ** 12:
    number = int(entered_value)
    answer, total_checks = test_prime(number)

    if answer:
        print(entered_value, "is a prime number (", total_checks, "checks )")
    else:
        print(entered_value, "is not a prime number (", total_checks, "checks )")
else:
    print("Please type a whole number from 0 to 1000000000000, for example 97.")

print()

# Display a comparison of both methods for different numbers.
print("        n  prime?  checks up to sqrt(n)  checks brute force")

examples = [1, 2, 9, 97, 100, 7919, 1000003]

for number in examples:
    prime_result, fast_checks = test_prime(number)
    slow_checks = get_brute_count(number)

    print(f"{number:>9}  {str(prime_result):<6}  {fast_checks:>20}  {slow_checks:>18}")
