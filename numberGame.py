# Guess the number game
import random
import sys

# Ask player for name
print('Hello, what is your name?')
name = input()

# Explain the game
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

# Assign random number
number = random.randint(1, 20)

# Give player 6 guesses
for num in range(6):
    guess = 0
    print(f'number of guesses remaining: {6 - num}')

    # Input validation and 
    while True:
        try:
            guess = int(input('Take a guess:'))
            while int(guess) < 1 or int(guess) > 20:
                print('You must enter an integer between 1 and 20.')
                guess = int(input('Take a guess:'))
        except ValueError:
            print('You must enter an integer between 1 and 20.')
            continue
        else:
            break

    if int(guess) == int(number):
        break
    elif int(guess) > int(number):
        print('Your guess is too high.')
        continue
    elif int(guess) < int(number):
        print('Your guess is too low.')
        continue

# Either too many tries or correct guess
if int(guess) == int(number):
    print(f'Good job, {name}! You guessed the number in {num + 1} tries')
else:
    print(f"Too bad! You couldn't guess in time. The number I was thinking of was {number}!")