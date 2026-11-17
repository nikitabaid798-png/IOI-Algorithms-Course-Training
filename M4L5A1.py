
# Activity 1: Exchanging Values Using XOR
# Topic: Swapping Two Numbers Without an Extra Variable

input("XOR can exchange two values without using another variable.  Press Enter ")

first, second = 5, 9

print("  before: a = 5   b = 9")

first = first ^ second
second = first ^ second
first = first ^ second

print("  after:  a =", first, "  b =", second)

number = int(input("Enter a number (try 3 or 7): "))
prediction = input(
    "After XOR swap of " + str(number) + " and 8 what does n become? "
)

left_value = number
right_value = 8

left_value ^= right_value
right_value ^= left_value
left_value ^= right_value

input("The XOR operations have exchanged both values.  Press Enter ")

print("  n became:", left_value, "  your guess:", prediction)
