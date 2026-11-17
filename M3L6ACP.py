
# DSCM4L6 After Class Project: Finding Two-Digit Prime Numbers
# Run using Python or Google Colab.
# The Sieve of Eratosthenes helps us find prime numbers efficiently.
# We mark the multiples of each prime number as False.


def sieve(limit):
    """Return all prime numbers up to the limit and count the crossings."""

    # Initially, assume every number is prime.
    prime_status = [True] * (limit + 1)
    prime_status[0] = False
    prime_status[1] = False

    crossing_count = 0
    current = 2

    while current * current <= limit:

        # TODO 1: Cross out multiples of the current prime number.
        if prime_status[current]:
            for multiple in range(current * current, limit + 1, current):
                if prime_status[multiple]:
                    prime_status[multiple] = False
                    crossing_count += 1

        current += 1

    # TODO 2: Collect all numbers that are still marked True.
    prime_numbers = []

    for number in range(2, limit + 1):
        if prime_status[number]:
            prime_numbers.append(number)

    return prime_numbers, crossing_count


# A: Generate prime numbers up to 99.
all_primes, crossings = sieve(99)

codes = []

# TODO 3: Select only the two-digit prime numbers.
for prime in all_primes:
    if prime >= 10:
        codes.append(prime)

print("Team codes (two-digit primes):", codes)
print("How many codes:", len(codes))

if len(codes) > 0:
    print("Smallest:", codes[0], " Largest:", codes[-1])

print("Crossings made by the sieve up to 99:", crossings)
print("Time: O(n log log n) for the sieve. Space: O(n) for the True/False list.")
