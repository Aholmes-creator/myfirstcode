# game.py

import random

secret_number = random.randint(1, 100)
max_guesses = 5
print("I'm thinking of a number between 1 and 100.")
guess_count = 0

while True:
    guess_str = input("What's your guess?")

    try:
        guess_int = int(guess_str)
        guess_count += 1
        if guess_count >= max_guesses:
            print(f"Sorry, you've run out of guesses! The number was {secret_number}.")
            break
    except ValueError:
        print("That's not a number! Please try again.")
        continue # This skips to the next loop iteration

    if guess_int < secret_number:
        print("Too Low!")
    elif guess_int > secret_number:
        print("Too High!")
    else:
        print(f"You got it! The number was {secret_number}.")
        break # This exits the loop
