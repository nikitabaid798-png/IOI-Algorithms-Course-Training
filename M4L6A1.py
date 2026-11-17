
# Activity 1: Understanding Power Sets and Binary Masks

input("Every element has two choices: included or excluded. Press Enter ")

print("  Set with 3 elements:", 2 ** 3, "possible subsets")
print("  Binary mask 5:", bin(5)[2:], "selects elements at positions 0 and 2")

element_count = int(input("How many elements are in your set? (try 4 or 5): "))
user_answer = input("Predict the total number of subsets: ")

input("The total is calculated by raising 2 to the number of elements. Press Enter ")

subset_count = 2 ** element_count

print("  Elements:", element_count)
print("  Total subsets:", subset_count)
print("  Your prediction:", user_answer)
