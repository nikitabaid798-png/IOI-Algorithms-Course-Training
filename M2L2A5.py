# ---- Tuple to List ----

# STEP 1 - Create a tuple
subjects = ("Math", "Science", "English", "Computer")

print("Original tuple:", subjects)

# STEP 2 - Convert tuple into a list
subject_list = list(subjects)

print("Converted list:", subject_list)

# STEP 3 - Modify the list
subject_list.append("History")
subject_list.remove("English")

print("Updated list:", subject_list)
