# Importing Modules
import random

print("Number Guessing Game Using Python :) ")

number = random.randint(1, 9)

while True:

    # User input
    guess = int(input("Guess a number (between 1 and 9): "))

    # Compare the user entered number with the number to be guessed
    if guess == number:
        print("CONGRATULATIONS! :) ")

        break
    
    else:
        print("WRONG! :/")
