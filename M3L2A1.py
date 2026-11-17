
# DSCM4L2 Activity 1: Understanding Big-O Notation

# Three different functions work with a list of scores.
# Each function counts the number of operations it performs.
# We compare the operation counts with their dominant terms.


def get_three_scores(data):
    # Access the first, middle and last elements.
    if len(data) == 0:
        return None, 0

    selected = [data[0], data[len(data) // 2], data[-1]]
    operations = 3

    return selected, operations


def calculate_average(data):
    # Find the total, highest score and average.
    if len(data) == 0:
        return None, 0

    total = 0
    highest = data[0]
    operations = 2

    for value in data:
        total += value

        if value > highest:
            highest = value

        operations += 2

    avg = total / len(data)
    operations += 1

    return avg, operations


def count_comparisons(data):
    # Compare every element with itself and the elements before it.
    count = 0
    operations = 0

    for x in range(len(data)):
        for y in range(x + 1):
            if data[y] <= data[x]:
                count += 1

            operations += 1

    return count, operations


print("     n |  O(1): steps  /1 |  O(n): steps     /n |  O(n^2): steps     /n^2")

for size in [10, 100, 1000, 2000]:
    marks = list(range(1, size + 1))

    constant_steps = get_three_scores(marks)[1]
    linear_steps = calculate_average(marks)[1]
    quadratic_steps = count_comparisons(marks)[1]

    ratio_constant = constant_steps / 1
    ratio_linear = linear_steps / size
    ratio_quadratic = quadratic_steps / (size * size)

    print(f"{size:>6} | {constant_steps:>11} {ratio_constant:>4.0f} | {linear_steps:>11} {ratio_linear:>6.3f} | {quadratic_steps:>13} {ratio_quadratic:>8.4f}")

print()
print("Exact counts: 3, 2n + 3 and n(n + 1)/2 = n^2/2 + n/2.")
print("Divided by the dominant term (1, n, n^2) they settle to 3, 2 and 0.5:")
print("drop the constant and the smaller terms -> O(1), O(n), O(n^2).")
