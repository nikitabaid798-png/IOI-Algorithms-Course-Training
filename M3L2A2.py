
# DSCM4L2 Activity 2: Understanding Search Performance

# Linear search checks each element until the required value is found.
# We will calculate the best, worst and average number of checks.


def find_element(data, value):
    # Return the position of the element and total checks.
    count = 0

    for position in range(len(data)):
        count += 1

        if data[position] == value:
            return position, count

    return -1, count


marks = [3, 7, 2, 9, 4, 1, 8, 5, 6]
size = len(marks)

print("List:", marks, "  n =", size)

check_list = []

for number in marks:
    position, checks = find_element(marks, number)
    check_list.append(checks)

    print(f"  search {number}: found at index {position} after {checks} check(s)")


absent_number = int(input("Pick a number that is not in the list: "))

position, absent_checks = find_element(marks, absent_number)

print(f"  search {absent_number}: index {position} (not in the list) after {absent_checks} checks")

print()

print("Best case :", min(check_list), "check   (target is first)        -> Theta(1)")
print("Worst case:", max(check_list + [absent_checks]), "checks  (target last or missing) -> Theta(n)")

average_checks = sum(check_list) / size

print("Average   :", average_checks, "checks  (every position equally likely) = (n + 1) / 2 =", (size + 1) / 2)

print("For every input: at most n checks -> O(n); at least 1 check -> Omega(1).")
