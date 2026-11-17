
# DSCM4L3 Activity 1: Comparing Linear and Binary Search

# Linear search checks elements one by one.
# Binary search repeatedly divides a sorted list into halves.
# We compare the number of checks required by both methods.


def search_linearly(data, number):
    # Look for the required number from left to right.
    count = 0

    for position in range(len(data)):
        count += 1

        if data[position] == number:
            return position, count

    return -1, count


def display_round(count, start, middle, end, current):
    # Display the details of the current binary search step.
    print("  check", count, ": low =", start, " mid =", middle, " high =", end, " value =", current)


def search_binary(data, number, show=False):
    # Binary search requires the list to be sorted.
    start = 0
    end = len(data) - 1
    count = 0

    while start <= end:
        middle = (start + end) // 2
        count += 1

        if show:
            display_round(count, start, middle, end, data[middle])

        if data[middle] == number:
            return middle, count

        elif data[middle] < number:
            start = middle + 1

        else:
            end = middle - 1

    return -1, count


marks = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print("Sorted list:", marks, "  n =", len(marks))

found_number = int(input("Search for a number that IS in the list: "))
missing_number = int(input("Search for a number that is NOT in the list: "))

for value in [found_number, missing_number]:
    print()
    print("Binary search for", value)

    position, checks = search_binary(marks, value, True)

    if position == -1:
        print(f"Result: {value} is not in the list ({checks} checks)")
    else:
        print(f"Result: {value} found at index {position} ({checks} checks)")


print()
print("target | linear checks | binary checks")

for value in [1, 9, 17, 4]:
    linear_count = search_linearly(marks, value)[1]
    binary_count = search_binary(marks, value)[1]

    print(f"{value:>6} | {linear_count:>13} | {binary_count:>13}")


print()
print("Worst case: search for a number bigger than every item")

for size in [9, 100, 1000, 1000000]:
    numbers = list(range(size))
    total_checks = search_binary(numbers, size)[1]

    print(f"  n = {size:>9,}   binary search checks = {total_checks}")
