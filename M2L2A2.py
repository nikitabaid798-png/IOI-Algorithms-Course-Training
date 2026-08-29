# ---- Set Operations ----

# STEP 1 - Create sets
morning_subjects = {"Math", "English", "Science", "History"}
afternoon_subjects = {"Science", "Computer", "Art", "English"}

print("Morning subjects:", morning_subjects)
print("Afternoon subjects:", afternoon_subjects)

# STEP 2 - Update the set
morning_subjects.add("Computer")
morning_subjects.discard("History")

print("\nUpdated morning subjects:", morning_subjects)
