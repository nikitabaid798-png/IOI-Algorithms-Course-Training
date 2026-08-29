# ---- Set Operations ----

# STEP 1 - Create two sets
morning_subjects = {"Math", "English", "Science", "Computer"}
afternoon_subjects = {"Science", "Computer", "Art", "History"}

print("Morning subjects:", morning_subjects)
print("Afternoon subjects:", afternoon_subjects)

# STEP 2 - Set operations
all_subjects = morning_subjects.union(afternoon_subjects)
common_subjects = morning_subjects.intersection(afternoon_subjects)
only_morning = morning_subjects.difference(afternoon_subjects)
different_subjects = morning_subjects.symmetric_difference(afternoon_subjects)

print("\nAll subjects (union):", all_subjects)
print("Common subjects (intersection):", common_subjects)
print("Only in morning (difference):", only_morning)
print("Not common (symmetric difference):", different_subjects)
