
# Activity 1: Exploring XOR Properties
# Topics: XOR Identity, Equality and Cancellation

input("XOR with zero leaves the value unchanged.  Press Enter ")

first_value = 5
second_value = 9

print("  5 XOR 0 =", first_value ^ 0)
print("  9 XOR 0 =", second_value ^ 0)

input("XOR of a number with itself becomes zero.  Press Enter ")

print("  5 XOR 5 =", first_value ^ first_value)
print("  9 XOR 9 =", second_value ^ second_value)

number = int(input("Enter a number (try 6 or 11): "))
prediction = input("What is 3 ^ " + str(number) + " ^ 3? ")

input("The repeated 3 values cancel each other.  Press Enter ")

answer = 3 ^ number ^ 3

print("  3 ^", number, "^ 3 =", answer, "  your guess:", prediction)
