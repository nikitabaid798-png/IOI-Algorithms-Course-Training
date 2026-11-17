
# Activity 1: Understanding Binary, AND and OR

number = int(input("Enter a number (try 5 or 12): "))
binary_guess = input("Guess its binary: ")

input("Binary.  Press Enter ")
binary_value = bin(number)[2:]
print("  decimal", number, "->  binary", binary_value)
print("  your guess:", binary_guess)

input("AND — both bits must be 1.  Press Enter ")
first_num = 12
second_num = 10

print("  12 =", format(first_num, "b"))
print("  10 =", format(second_num, "b"))
print("  12 & 10 =", first_num & second_num)

input("OR — at least one bit must be 1.  Press Enter ")
or_answer = first_num | second_num
print("  12 | 10 =", or_answer)
