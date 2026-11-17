
# DSCM4L1 Activity 2: Comparing the growth of algorithms

# We will test three algorithms with different values of n.
# As the number of students increases, we compare how the
# number of steps changes for each approach.


def get_formula_count(value):
    answer = value * (value + 1) // 2
    return 1


def get_loop_count(value):
    answer = 0
    count = 0

    for i in range(1, value + 1):
        answer += i
        count += 1

    return count


def get_nested_loop_count(value):
    answer = 0
    count = 0

    for i in range(1, value + 1):
        for j in range(1, i + 1):
            answer += 1
            count += 1

    return count


print("     n   Formula      Loop   Double loop")

for size in [4, 10, 100, 1000, 2000]:
    formula_result = get_formula_count(size)
    loop_result = get_loop_count(size)
    nested_result = get_nested_loop_count(size)

    print(f"{size:>6} {formula_result:>9} {loop_result:>9} {nested_result:>13}")


print()
print("n doubles from 1000 to 2000. How many times more steps?")
print("  Formula     x", get_formula_count(2000) / get_formula_count(1000))
print("  Loop        x", get_loop_count(2000) / get_loop_count(1000))
print("  Double loop x", round(get_nested_loop_count(2000) / get_nested_loop_count(1000), 2))
