# ---- Number Guessing Game ----

# STEP 1 - Store the secret number
secret_number = 25

# STEP 2 - Ask the user to enter a guess
guess = int(input("Enter your guess: "))

# STEP 3 - Check the guess
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")
