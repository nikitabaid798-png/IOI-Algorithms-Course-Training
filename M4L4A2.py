
# Activity 2: Identifying Powers of 4 and 8
# Power of 4: power of 2 with an even bit position
# Power of 8: power of 2 with a bit position divisible by 3

input("Power of 4 uses n % 3 == 1; power of 8 uses n % 7 == 1.  Press Enter ")

print("  16  binary:", bin(16)[2:],
      "  16 % 3 =", 16 % 3, "  power of 4: yes")

print("  8   binary:", bin(8)[2:],
      "  8 % 7 =", 8 % 7, "  power of 8: yes")

number = int(input("Enter a number (try 64 or 32): "))
guess = input("Is " + str(number) + " a power of 4? (yes/no): ")

input("Use the remainder condition n % 3 == 1.  Press Enter ")

power_four = (
    number > 0
    and (number & (number - 1)) == 0
    and number % 3 == 1
)

if power_four:
    print(" ", number, "  binary:", bin(number)[2:],
          "  power of 4: yes  your guess:", guess)
else:
    print(" ", number, "  binary:", bin(number)[2:],
          "  power of 4: no   your guess:", guess)
