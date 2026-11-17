
# DSCM4L6 Activity 1: Testing Whether a Number Is Prime
# Run using Python or Google Colab.
# One check means testing whether a number divides evenly.
# We only need to test divisors up to the square root of the number.


def check_prime(number):
    """Return whether a number is prime along with the total number of checks."""
    check_count = 0

    if number < 2:
        return False, check_count

    divisor = 2

    while divisor * divisor <= number:
        check_count += 1

        if number % divisor == 0:
            return False, check_count

        divisor += 1

    return True, check_count


def count_brute_checks(number):
    """Count checks using the slower method of testing every number up to n - 1."""
    total_checks = 0

    for divisor in range(2, number):
        total_checks += 1

        if number % divisor == 0:
            break

    return total_checks


# Get a number from the user and validate the input.
user_text = input("Type a whole number to test: ").strip()

if user_text.isdecimal() and len(user_text) <= 13 and int(user_text) <= 10 ** 12:
    number = int(user_text)
    result, check_count = check_prime(number)

    if result:
        print(user_text, "is a prime number (", check_count, "checks )")
    else:
        print(user_text, "is not a prime number (", check_count, "checks )")
else:
    print("Please type a whole number from 0 to 1000000000000, for example 97.")

print()

# Compare the optimized method with brute force.
print("        n  prime?  checks up to sqrt(n)  checks brute force")

test_numbers = [1, 2, 9, 97, 100, 7919, 1000003]

for value in test_numbers:
    prime_status, optimized_checks = check_prime(value)
    brute_checks = count_brute_checks(value)

    print(f"{value:>9}  {str(prime_status):<6}  {optimized_checks:>20}  {brute_checks:>18}")
