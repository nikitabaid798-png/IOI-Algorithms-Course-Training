
# =================================
# BINARY SUBSET CREATOR
# =================================
# Concepts:
# Power Set, Binary Masks, Bit Probing,
# Subset Enumeration, and Bit Difference

elements = ["A", "B", "C"]
element_total = len(elements)
subset_total = 2 ** element_total

print("================================")
print("BINARY SUBSET CREATOR")
print("================================")

print("Available elements:", elements)
print("Element count:", element_total)
print("Possible subsets:", subset_total)


# ---------------------------------
# PART 1 - POWER SET
# ---------------------------------

print("\nPART 1: Understanding the Power Set")

print("With", element_total, "elements, there are", subset_total, "possible subsets.")


# ---------------------------------
# PART 2 - USING BINARY MASKS
# ---------------------------------
# Each mask represents one possible combination.
# A 1 means selected, while a 0 means not selected.

print("\nPART 2: Binary Mask Combinations")

current_mask = 0

while current_mask < subset_total:

    third_bit = (current_mask >> 2) & 1
    second_bit = (current_mask >> 1) & 1
    first_bit = current_mask & 1

    print("Mask", current_mask, "-> [C][B][A] =", third_bit, second_bit, first_bit)

    current_mask += 1


# ---------------------------------
# PART 3 - CHECKING A PARTICULAR BIT
# ---------------------------------
# Shifting 1 to the left creates a probe for a chosen position.
# AND checks whether that position is switched on.

print("\nPART 3: Checking Individual Bits")

test_mask = 5

print("Chosen mask:", test_mask)
print("Binary representation:", bin(test_mask))

position = 0

while position < element_total:

    bit_probe = 1 << position

    if test_mask & bit_probe:
        print("Position", position, "is ON -", elements[position], "is included.")
    else:
        print("Position", position, "is OFF -", elements[position], "is excluded.")

    position += 1


# ---------------------------------
# PART 4 - GENERATING EVERY SUBSET
# ---------------------------------
# The first loop selects a mask.
# The second loop checks which elements belong to it.

print("\nPART 4: Generating All Possible Subsets")

current_mask = 0

while current_mask < subset_total:

    selected_items = []
    position = 0

    while position < element_total:

        bit_probe = 1 << position

        if current_mask & bit_probe:
            selected_items.append(elements[position])

        position += 1

    print("Mask", current_mask, "represents:", selected_items)

    current_mask += 1


# ---------------------------------
# PART 5 - COUNTING DIFFERENT BITS
# ---------------------------------

def count_bit_changes(first, second):

    changes = 0

    while first > 0 or second > 0:

        bit_first = first & 1
        bit_second = second & 1

        if bit_first != bit_second:
            changes += 1

        first >>= 1
        second >>= 1

    return changes


print("\nPART 5: Comparing Binary Numbers")

print("Difference between 12 and 15:", count_bit_changes(12, 15))
print("12 =", bin(12), "15 =", bin(15))

print("Difference between 21 and 24:", count_bit_changes(21, 24))
print("21 =", bin(21), "24 =", bin(24))

print("Difference between 8 and 8:", count_bit_changes(8, 8))
print("8 =", bin(8), "8 =", bin(8))


# ---------------------------------
# FINAL SUMMARY
# ---------------------------------

print("\n================================")
print("BINARY SUBSET CREATOR - SUMMARY")
print("================================")

print("Power Set: Contains every possible subset.")
print("Binary Mask: Represents selected elements through bits.")
print("Bit Probe: Checks a particular position using 1 << j.")
print("Nested Loops: Generate and inspect all possible subsets.")
print("Bit Difference: Counts positions where two binary numbers differ.")

print("================================")
