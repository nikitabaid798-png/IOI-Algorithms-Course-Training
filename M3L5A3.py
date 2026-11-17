
# Find all prime palindrome numbers from 1 to 3000

limit = 3000

for number in range(1, limit + 1):
    factor_count = 0
    reversed_number = 0
    original = number

    # Count the factors of the current number.
    for divisor in range(1, original + 1):
        if original % divisor == 0:
            factor_count += 1

    # Continue only if the number is prime.
    if factor_count == 2:

        # Reverse the digits of the number.
        temporary = original

        while temporary > 0:
            last_digit = temporary % 10
            reversed_number = reversed_number * 10 + last_digit
            temporary //= 10

        # Check whether the original and reversed numbers match.
        if reversed_number == number:
            print(number)
