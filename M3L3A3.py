
# DSCM4L3 Activity 3: Exploring the Complexity Ladder

# We will compare four types of algorithms:
# Constant, logarithmic, linear and quadratic.
# Their number of steps is counted and compared when n doubles.


def get_constant_count(size):
    # Only one operation is required.
    return 1


def get_log_count(size):
    # Repeatedly divide the search range into smaller parts.
    start = 0
    end = size - 1
    count = 0

    while start <= end:
        middle = (start + end) // 2
        count += 1
        start = middle + 1

    return count


def get_linear_count(size):
    # Visit each item once.
    count = 0

    for i in range(size):
        count += 1

    return count


def get_quadratic_count(size):
    # Run one loop inside another loop.
    count = 0

    for i in range(size):
        for j in range(size):
            count += 1

    return count


complexity_types = [
    ("O(1)", get_constant_count),
    ("O(log n)", get_log_count),
    ("O(n)", get_linear_count),
    ("O(n^2)", get_quadratic_count)
]

print("rung       steps at n=1000   steps at n=2000   n doubled: steps x")

for label, function in complexity_types:
    count_1000 = function(1000)
    count_2000 = function(2000)

    growth_ratio = count_2000 / count_1000 if count_1000 else 0

    print(f"{label:<10} {count_1000:>15,} {count_2000:>17,} {growth_ratio:>17.2f}")

print("(every number above was counted by running the loops)")
print()

size = int(input("Big n to test (the demo uses 1000000): "))

print("At n = 1,000,000:  O(1) =", get_constant_count(size),
      "  O(log n) =", get_log_count(size),
      "  O(n) =", f"{get_linear_count(size):,}")

print("O(n^2) would be", f"{size * size:,}", "steps: too many to count here.")
