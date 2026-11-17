
# DSCM4L1 Activity 3: Comparing memory usage

# We will calculate the sum of numbers from 1 to n in two ways.
# The first method uses a running total, while the second stores
# all the numbers in a list before calculating their sum.
# We will also compare their memory usage.

import tracemalloc


def calculate_running(num):
    # Store only the current total and loop variable.
    result = 0

    for i in range(1, num + 1):
        result += i

    return result, 2


def calculate_list(num):
    # First save all numbers in a list.
    number_list = []

    for i in range(1, num + 1):
        number_list.append(i)

    result = 0

    # Add all the stored numbers.
    for value in number_list:
        result += value

    return result, len(number_list)


def measure_memory(function, num):
    # Find the maximum memory used while running the function.
    tracemalloc.start()
    function(num)

    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return memory_used


print("n = 4 :", "running total keeps", calculate_running(4)[1], "numbers (total and k);",
      "the list keeps", calculate_list(4)[1], "numbers; both totals =", calculate_running(4)[0])

print()

print("       n | numbers kept: running   list | peak bytes: running      list")

for size in [1000, 10000, 100000]:
    running_count = calculate_running(size)[1]
    list_count = calculate_list(size)[1]

    running_memory = measure_memory(calculate_running, size)
    list_memory = measure_memory(calculate_list, size)

    print(f"{size:>8} | {running_count:>21} {list_count:>6} | {running_memory:>19} {list_memory:>9}")

print()
print("Running total: memory stays the same. List: 10 times more n, about 10 times more memory.")
