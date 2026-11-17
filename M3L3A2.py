
# DSCM4L3 Activity 2: Exploring Recursion

# A recursive function calls itself with a smaller number.
# We count the total function calls and the maximum depth reached.
# We also compare recursion with a normal while loop.

import sys


def recursive_count(value, level, display):
    # Return the total calls and maximum depth.
    if display:
        print("  " * level + "recursive_count(" + str(value) + ")   depth", level)

    # Stop when the value becomes zero or negative.
    if value <= 0:
        return 1, level

    total_calls, max_depth = recursive_count(value - 1, level + 1, display)

    return total_calls + 1, max_depth


def loop_count(value):
    # Perform the same countdown without recursion.
    iterations = 0

    while value >= 0:
        iterations += 1
        value -= 1

    return iterations


number = int(input("Count down from which number? "))

print("Trace of countdown(" + str(number) + "):")

total_calls, max_depth = recursive_count(number, 1, True)

print("calls =", total_calls, "  deepest depth =", max_depth)

print()
print("     n | recursive calls | deepest depth | loop steps")

for size in [10, 100, 500]:
    total_calls, max_depth = recursive_count(size, 1, False)

    print(f"{size:>6} | {total_calls:>15} | {max_depth:>13} | {loop_count(size):>10}")


print()
print("Python's limit on waiting calls here:", sys.getrecursionlimit())

try:
    total_calls, max_depth = recursive_count(5000, 1, False)
    print("countdown(5000) finished:", total_calls, "calls")

except RecursionError:
    print("countdown(5000) -> RecursionError: the call stack is full")

print("countdown_loop(5000) ->", loop_count(5000), "steps (a loop needs no stack)")
