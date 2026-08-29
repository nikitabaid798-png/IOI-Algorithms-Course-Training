# ---- Product Directory ----

# STEP 1 - Create two lists
product_ids = [101, 102, 103, 104, 105]
product_names = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

print("Product IDs:", product_ids)
print("Product Names:", product_names)

# STEP 2 - Convert lists into a dictionary
product_directory = dict(zip(product_ids, product_names))
print("\nProduct Directory:", product_directory)

# STEP 3 - Access values from the dictionary
print("Product with ID 101:", product_directory[101])
print("Product with ID 103:", product_directory[103])
print("Product with ID 105:", product_directory[105])
