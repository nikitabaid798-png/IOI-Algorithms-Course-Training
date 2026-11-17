
# DSCM4L2 Activity 3: Understanding Loop Complexity

# We will compare four different loop structures.
# Each program counts how many times its main statement executes.
# Increasing n helps us understand how the number of steps grows.


def sequential_loops(size):
    count = 0

    for a in range(size):
        count += 1

    for b in range(size):
        count += 1

    return count


def nested_loops(size):
    count = 0

    for a in range(size):
        for b in range(size):
            count += 1

    return count


def limited_inner_loop(size):
    count = 0

    for a in range(size):
        for b in range(5):
            count += 1

    return count


def increasing_inner_loop(size):
    count = 0

    for a in range(size):
        for b in range(a + 1):
            count += 1

    return count


loop_types = [
    ("two loops in a row", sequential_loops),
    ("loop inside a loop", nested_loops),
    ("inner loop runs 5 times", limited_inner_loop),
    ("inner loop runs i + 1 times", increasing_inner_loop)
]

print("shape                        n=10   n=100    n=1000  100->1000  Big-O")

for description, function in loop_types:
    result_10 = function(10)
    result_100 = function(100)
    result_1000 = function(1000)

    growth = result_1000 / result_100 if result_100 > 0 else 0

    if growth < 30:
        complexity = "O(n)"
    else:
        complexity = "O(n^2)"

    print(f"{description:<27} {result_10:>5} {result_100:>7} {result_1000:>9}  x{growth:>7.1f}  {complexity}")

print()
print("Loops in a row add (n + n = 2n). Loops inside loops multiply (n x n),")
print("unless the inner loop runs a fixed number of times (5 x n is still O(n)).")
