
# DSCM4L1 Activity 1: Comparing three algorithms

# Problem: Each student earns points equal to their roll number.
# Find the total points earned by all students.
# We will compare three different approaches by counting the steps.

def calculate_formula(num):
    # Calculate the sum directly using a mathematical formula.
    result = num * (num + 1) // 2
    count = 1
    return result, count


def calculate_loop(num):
    # Add the points earned by each student one by one.
    result = 0
    count = 0

    for i in range(1, num + 1):
        result += i
        count += 1

    return result, count


def calculate_nested_loop(num):
    # Count each point separately using two loops.
    result = 0
    count = 0

    for i in range(1, num + 1):
        for j in range(i):
            result += 1
            count += 1

    return result, count


students = int(input("How many students are in the contest? "))

print("Contest with n =", students, "students (student k earns k points)")
print()

total, steps = calculate_formula(students)
print("Formula     : total =", total, "  steps =", steps)

total, steps = calculate_loop(students)
print("Loop        : total =", total, "  steps =", steps)

total, steps = calculate_nested_loop(students)
print("Double loop : total =", total, "  steps =", steps)

print()
print("Same total, different number of steps.")
