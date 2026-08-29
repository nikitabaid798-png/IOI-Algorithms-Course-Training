# ---- Tuple Operations ----

# Create a tuple
sports = ("Cricket", "Football", "Tennis", "Basketball")

print("Sports:", sports)

# Access tuple elements
print("First sport:", sports[0])
print("Last sport:", sports[-1])

# Slicing
print("First three sports:", sports[:3])

# Length of tuple
print("Total sports:", len(sports))

# Iterate through tuple
print("\nSports list:")
for sport in sports:
    print("-", sport)
