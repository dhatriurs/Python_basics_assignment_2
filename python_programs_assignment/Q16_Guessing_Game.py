# Q16 - Guessing Game (Alternative Version)

import random

secret = random.randint(1, 50)

for attempt in range(5):
    try:
        guess = int(input("Guess the number (1-50): "))

        if guess == secret:
            print("Correct guess!")
            break
        elif guess > secret:
            print("Too high.")
        else:
            print("Too low.")
    except:
        print("Invalid input.")
else:
    print("Game over. Number was", secret)