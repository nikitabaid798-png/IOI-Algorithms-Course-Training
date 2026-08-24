# Ask the user how many rows they want
rows = int(input("Enter the number of rows: "))

# Print the star pattern
for row in range(1, rows + 1):
    for star in range(row):
        print("*", end="")
    print()
